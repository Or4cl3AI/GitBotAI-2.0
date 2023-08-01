import os
from flask import Flask, jsonify, request
from github_api import GithubAPI
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

github_api = GithubAPI()

@app.route('/api/generate_code', methods=['POST'])
def generate_code():
    data = request.get_json()
    response = github_api.generate_code(data)
    return jsonify(response)

@app.route('/api/manage_repo', methods=['POST'])
def manage_repo():
    data = request.get_json()
    response = github_api.manage_repo(data)
    return jsonify(response)

@app.route('/api/version_control', methods=['POST'])
def version_control():
    data = request.get_json()
    response = github_api.version_control(data)
    return jsonify(response)

@app.route('/api/authenticate', methods=['POST'])
def authenticate():
    data = request.get_json()
    response = github_api.authenticate(data)
    return jsonify(response)

if __name__ == '__main__':
    app.run(host=os.environ.get('HOST', '0.0.0.0'), port=int(os.environ.get('PORT', 5000)))