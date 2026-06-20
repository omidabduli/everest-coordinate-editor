@echo off
TITLE Everest - Coordinate Editor
if not exist "venv" (
    python -m venv venv
)
call venv\Scripts\activate
pip install --quiet -r requirements.txt
python app.py
pause
