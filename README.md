# Geometry Dash Resources Organizer

A GUI tool to help organize and unorganize your Geometry Dash "Resources" folder.

## Features

- **Organize**: Sorts Geometry Dash resources into categorized folders based on file name patterns.
- **Unorganize**: Flattens organized folders back into Geometry Dash’s default layout.
- **GUI Interface**: No command line needed—everything runs in a friendly window.
- **Version Support**: Fully compatible with Geometry Dash **2.2074**.

## How to Use

### Option 1: Download the Release (.exe)

1. Head over to the [Releases](https://github.com/Runtem/gd-resources-organizer/releases/latest) section.
2. Download the latest `.exe` file.
3. Run it—no setup, no Python required.

### Option 2: Run from Source (Python)

1. Clone or download this repository.
2. Launch the app using:

    ```bash
    python3 main.py
    ```

3. A window will open. From there:
   - Select the **source folder** (where your GD resources are or an already organized folder).
   - Select the **destination folder** (where you want the output).
   - Select the option "Organize" or "Unorganize" and... **you know where else to click from there.**

> **Important:** Always make sure both the source and destination folders are set properly before proceeding.

## Requirements (for source use)

- Python 3.7 or newer
- `tkinter` (usually pre-installed with Python)

## Disclaimer

This project is fully written in **Python**.  
If that bothers you... **skill issue**.
