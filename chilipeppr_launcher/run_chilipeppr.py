import http.server
import socketserver
import webbrowser
import threading
import os
import subprocess
import time
import sys
import tkinter as tk
from tkinter import messagebox

PORT = 8000

class ServerThread(threading.Thread):
    def __init__(self, folder, port):
        super().__init__()
        self.folder = folder
        self.port = port
        self.httpd = None

    def run(self):
        os.chdir(self.folder)
        handler = http.server.SimpleHTTPRequestHandler
        with socketserver.TCPServer(("", self.port), handler) as self.httpd:
            print(f"Serving ChiliPeppr at http://localhost:{self.port}")
            self.httpd.serve_forever()

    def stop(self):
        if self.httpd:
            print("Shutting down HTTP server...")
            self.httpd.shutdown()
            print("HTTP server stopped.")


def start_spjs(spjs_path):
    print("Starting Serial Port JSON Server...")
    try:
        si = subprocess.STARTUPINFO()
        si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        spjs_process = subprocess.Popen(
            [spjs_path, "-disablecayenn"],
            startupinfo=si,
            shell=False
        )
        print("SPJS started.")
        return spjs_process
    except Exception as e:
        print(f"Failed to start SPJS: {e}")
        return None


def on_close():
    if messagebox.askokcancel("Quit", "Do you want to stop the server and exit?"):
        if spjs_process:
            print("Terminating SPJS process...")
            spjs_process.terminate()
            spjs_process.wait()
            print("SPJS process terminated.")

        if server_thread:
            server_thread.stop()
            server_thread.join()

        root.destroy()


def show_splash():
    splash = tk.Tk()
    splash.overrideredirect(True)
    splash.geometry("500x300+500+300") 
    splash.configure(bg='alice blue')
    label = tk.Label(splash, text="Launching ChiliPeppr...\n Opening Browser...", font=("Arial", 16))
    label.pack(expand=True)

    def close_splash():
        splash.destroy()

    splash.after(4000, close_splash)  
    splash.mainloop()


if __name__ == "__main__":

    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")

    CHILIP_EPPR_FOLDER = os.path.join(base_path, "chilipeppr.local")
    SPJS_PATH = os.path.join(base_path, "serial-port-json-server.exe")

    if not os.path.exists(CHILIP_EPPR_FOLDER):
        print(f"ERROR: ChiliPeppr folder not found: {CHILIP_EPPR_FOLDER}")
        sys.exit(1)
    if not os.path.exists(SPJS_PATH):
        print(f"ERROR: SPJS executable not found: {SPJS_PATH}")
        sys.exit(1)

    show_splash()

    server_thread = ServerThread(CHILIP_EPPR_FOLDER, PORT)
    server_thread.daemon = True
    server_thread.start()

    spjs_process = start_spjs(SPJS_PATH)
    if not spjs_process:
        print("Failed to start SPJS. Exiting.")
        sys.exit(1)

    time.sleep(2)  


    webbrowser.open(f"http://localhost:{PORT}/workspace_grbl.html")

    root = tk.Tk()
    root.title("ChiliPeppr Server Controller")
    root.geometry("350x150")

    label = tk.Label(root, text=f"ChiliPeppr server running at http://localhost:{PORT}", wraplength=320)
    label.pack(pady=20)

    btn_close = tk.Button(root, text="Close Server", command=on_close)
    btn_close.pack(pady=10)

    root.protocol("WM_DELETE_WINDOW", on_close)

    root.mainloop()
