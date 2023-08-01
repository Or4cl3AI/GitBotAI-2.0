import requests
from flask import request, jsonify

serverUrl = "http://localhost:5000"

def sendRequest(endpoint, method="GET", data=None):
    if data is None:
        data = {}
    url = f"{serverUrl}/{endpoint}"
    if method == "GET":
        response = requests.get(url, params=data)
    elif method == "POST":
        response = requests.post(url, json=data)
    elif method == "PUT":
        response = requests.put(url, json=data)
    elif method == "DELETE":
        response = requests.delete(url, json=data)
    else:
        return None

    return response.json()

@app.route('/message', methods=['POST'])
def handle_message():
    data = request.get_json()
    action = data.get('action')
    params = data.get('params')

    if action == 'generateCode':
        response = sendRequest('generateCode', 'POST', params)
    elif action == 'manageRepo':
        response = sendRequest('manageRepo', 'POST', params)
    else:
        response = {"error": "Invalid action"}

    return jsonify(response)
