# 🏔️ Everest — Spatial Coordinate & XYZ Data Editor

[![Python Version](https://img.shields.io/badge/Python-3.9+-blue.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0+-000000.svg?style=flat&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Docker](https://img.shields.io/badge/Docker-Supported-2496ED.svg?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)
[![Release](https://img.shields.io/github/v/release/omidabduli/everest-coordinate-editor?style=flat&label=release)](https://github.com/omidabduli/everest-coordinate-editor/releases/latest)
[![Developer](https://img.shields.io/badge/Developed%20by-Omid%20Abduli-1648D8.svg?style=flat)](https://github.com/omidabduli)

**Everest** is a browser-based coordinate editor and spatial data tool designed for environmental modeling and GIS workflows. It allows you to transform, shift, and mirror spatial point data, automatically identify Coordinate Reference Systems (CRS) using Mistral AI, and export clean XYZ files formatted for MIKE by DHI mesh generators.

---

## ⚡ Features

* **CRS & EPSG Detection**: Send coordinate samples to Mistral AI (`mistral-small-latest`) to identify projection systems and EPSG codes.
* **Bulk Coordinate Transformations**: Shift offsets, scale coordinates, perform basic math operations, and apply decimal rounding across entire datasets.
* **Spatial Axis Mirroring**: Mirror point data along X, Y, or Z axes based on the dataset's bounding box center.
* **Live Spatial Statistics**: Instant minimum and maximum coordinate boundary summaries (X, Y, Z).
* **MIKE by DHI XYZ Export**: Export clean space-separated XYZ files ready for MIKE 21 / MIKE 3 mesh generators, as well as standard CSV and TXT files.
* **Docker Support**: Containerized deployment with Docker and Docker Compose.

---

## 🚀 Quick Start

### 1. Local Python Setup

```bash
# Clone repository
git clone https://github.com/omidabduli/everest-coordinate-editor.git
cd everest-coordinate-editor

# Install dependencies
pip install -r requirements.txt

# (Optional) Set Mistral API key for server-side CRS detection
export MISTRAL_API_KEY=your_mistral_api_key_here

# Run the app
python app.py
```

Open `http://localhost:5007` in your browser.

*Note for desktop users:* You can also launch the app using `RUN_EVEREST.command` (macOS/Linux) or `RUN_EVEREST.bat` (Windows).

---

### 2. Docker Deployment

#### Using Docker Compose (Recommended)

```bash
docker-compose up -d
```

Access the application at `http://localhost:5007`.

#### Using Docker CLI

```bash
# Build container image
docker build -t everest-coordinate-editor .

# Run container
docker run -d -p 5007:5007 --env-file .env everest-coordinate-editor
```

---

## 🛠️ Project Structure

```text
everest-coordinate-editor/
├── index.html              # Main web interface (HTML/CSS/JS)
├── app.py                  # Flask backend & Mistral AI proxy endpoint
├── Dockerfile              # Docker container definition
├── docker-compose.yml      # Docker Compose configuration
├── requirements.txt        # Python dependencies
├── RUN_EVEREST.command     # macOS/Linux launcher script
├── RUN_EVEREST.bat         # Windows launcher script
└── .env                    # Environment variables (API key configuration)
```

---

## Author

**Developed and maintained by [Omid Abduli](https://github.com/omidabduli)**  
[Roland Digital](https://roland-digital.de/) · Germany

