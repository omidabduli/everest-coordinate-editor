from flask import Flask, send_from_directory, request, jsonify
import os
import requests
from dotenv import load_dotenv

# Load local environment variables from .env file
load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'Interface.html')

@app.route('/api/detect-crs', methods=['POST'])
def detect_crs():
    try:
        data = request.get_json() or {}
        prompt = data.get('prompt')
        if not prompt:
            return jsonify({'error': 'Prompt is required'}), 400
        
        api_key = os.environ.get('MISTRAL_API_KEY')
        if not api_key:
            return jsonify({'error': 'Mistral API key is not configured on the server. Please set MISTRAL_API_KEY in your environment or a .env file.'}), 500
        
        resp = requests.post(
            'https://api.mistral.ai/v1/chat/completions',
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {api_key}'
            },
            json={
                'model': 'mistral-small-latest',
                'messages': [{'role': 'user', 'content': prompt}],
                'temperature': 0.0,
                'max_tokens': 500
            },
            timeout=15
        )
        
        if not resp.ok:
            return jsonify({'error': f'Mistral API returned status {resp.status_code}: {resp.text}'}), resp.status_code
        
        return jsonify(resp.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5007, debug=True)
