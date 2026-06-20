#!/bin/bash
cd "$(dirname "$0")"
echo "==========================================="
echo "   🪄  EVEREST - STARTING SERVER...     "
echo "==========================================="
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi
source venv/bin/activate
pip install --quiet -r requirements.txt
python app.py
