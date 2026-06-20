# 🏔️ Everest — XYZ Coordinate Editor v1.0

[![Python Version](https://img.shields.io/badge/Python-3.9+-blue.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Developer](https://img.shields.io/badge/Made%20by-OA-lightgrey.svg?style=flat)](https://github.com/noybiss)

A powerful in-browser editor for spatial coordinate files and XYZ data management.

## 🌊 Overview

Everest allows users to load, inspect, edit, and export point cloud data. It features automatic coordinate system detection and bulk editing capabilities.

## ⚙️ Main Entry Point

Run the application with:
```bash
python app.py
```

Or use the launcher scripts:
- **macOS/Linux**: `./RUN_EVEREST.command`
- **Windows**: `RUN_EVEREST.bat`

## ✨ Features

- 🤖 **AI-Powered CRS Detection**: Automatically identifies coordinate reference systems and shows the exact name needed in MIKE DHI.
- ⚡ **Bulk Column Editing**: Multiply, divide, add, subtract, round, or replace values across all rows in a single operation.
- ↔ **Mirror & Flip**: Reflected point cloud operations around the automatic bounding-box center.
- 💾 **Flexible Export**: Clean support for MIKE by DHI XYZ format (space-separated, no headers), CSV, and tab-delimited TXT.

## 🗂️ Project Directory Structure

```text
Everest/
├── Interface.html          # Frontend web interface (HTML/CSS/JS)
├── app.py                  # Python Flask server & Mistral CRS proxy
├── requirements.txt        # Project dependencies list
├── RUN_EVEREST.bat         # Windows quick launcher
├── RUN_EVEREST.command     # macOS/Linux execution command script
├── .env.example            # Local environment template configuration
└── .gitignore              # Git ignore rules
```

---

**Developed & Maintained by [OA](https://github.com/noybiss)**  
*Universal Environmental Intelligence Engine.*
