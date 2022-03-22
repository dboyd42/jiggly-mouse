# Jiggly Mouse

> **Author:** David Boyd<br>
> **Date:** 2022-03-21

![](./imgs/windows.gif)

This program jiggles your mouse to prevent your computer from going to sleep or
to screensaver mode.  I wrote this program because most of the mouse jiggler
programs were written for only Windows.  This has been tested in both macOS
(Monterey) and Windows 11.  For argument's sake, I'll just assume this works in
Linux as this program was purposefully written in Python3 to be cross-platform.

## Installation

### Running the Binary -- Overview

Provided binaries:

  - :white_check_mark: Windows: `./binaries/jiggly-mouse-win-x64.exe`
  - :white_check_mark: macOS: `./binaries/jiggly-mouse-macOS.app`
  - :timer_clock: Linux: `./binaries/jiggly-mouse-linux.elf`
  - :x: WSL2 + Kali-Win-Kex (TigerVNC): No luck :shrug:

1. Download the platform relative binary to desired directory (ie. Desktop)

2. Open the program where and accept the prompts

### macOS - Monterey

---

Bypassing Apple's [Unidentified Developer](https://support.apple.com/guide/mac-help/open-a-mac-app-from-an-unidentified-developer-mh40616/mac)

  1. Unzip application (if applicable)
  2. In the Finder  on your Mac, locate the app you want to open.<br> 
     Don’t use Launchpad to do this. Launchpad doesn’t allow you to access the shortcut menu.
  4. Control-click the app icon, then choose Open from the shortcut menu.
  5. Click Open.<br>
  
  The app is now saved as an exception to your security settings, and you can open it in the future by double-clicking it just as you can any registered app.
      
  6. Upon prompt: `Security & Privacy` > `Accessibility` > Allow `jiggly-mouse-macOS.app`<br>
     - This is required because the program is taking over your mouse

### Windows 11

---

  - Prompt: `Windows protected your PC` 
    1. Click `More info`
    2. Click `Run anyway`

### Linux

---

  - *(will update once tested)*

## Running via Python3-CLI

### Dependencies

---

- **PIP:** `PyAutoGui` for GUI mouse control
- ***macOS:*** `Tkinter` has issues, so good luck.  I messed up my soft-linked
  files by installing it via brew... dunno what else it messed up.
    - Running the `jiggly-mouse-macOS.app` binary resolves this issue.

#### Run via CLI

---

  - `python3 jiggly-mouse.py` or use whatever setup you have at this point.
  - Or allow permissions: `chmod u+x jiggly-mouse.py && ./jiggly-mouse.py`

