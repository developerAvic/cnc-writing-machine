# cnc-writing-machine

# 🛠️ Local ChiliPeppr & GRBL Firmware

This project provides a fully local environment for controlling a GRBL-based CNC or writing machine. It includes everything needed to run the **ChiliPeppr workspace**, **Serial Port JSON Server (SPJS)**, and a launcher script (run_chillipeppr) found in (chilipeppr_launcher\dist\run_chilipeppr.exe)  to simplify the process.

You can control your plotter, CNC machine, or writing robot directly from your computer using this setup — no internet required.

---

## 📦 What's Included

- `chillipeppr/` - GRBL-compatible ChiliPeppr workspace files (served locally)
- `spjs/` - Serial Port JSON Server to communicate with GRBL over USB
- `Run Chillipeppr` - Script to start SPJS, serve the workspace, and open the browser
- `grbl firmware files` - firmware can be found on (code and configuration files\grbl-mi\grbl-mi)
- `grbl configuration file` - all the commands u need to set up the grbl on ur microcontroller
- `inkscape extensions` - inkscape extenstions for controlling the pen movements
- `stl files` - 3d designed parts which i modelled for my project
---

## Note 
- this repository is a combination of two or more repositories and files 

## 🔧 Requirements

- A **GRBL-compatible microcontroller** (typically Arduino Uno)
- **GRBL firmware** installed on the microcontroller   
  → Use Arduino IDE or `XLoader` to flash it
- Serial Port JSON Server (included)
- Modern web browser

---

## Clone this Repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name


