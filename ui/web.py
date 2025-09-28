from flask import Flask, request, jsonify
import subprocess
import logging

app = Flask(__name__)

@app.route('/run_playbook', methods=['POST'])
def run_playbook():
    data = request.get_json()
    incident_type = data.get('incident_type')
    params = data.get('params', [])
    
    logging.info(f"Running playbook for incident type: {incident_type} via web interface")
    result = subprocess.run(["python", "main.py", incident_type] + params, capture_output=True, text=True)
    
    return jsonify({"output": result.stdout, "errors": result.stderr})

if __name__ == "__main__":
    app.run(debug=True)
