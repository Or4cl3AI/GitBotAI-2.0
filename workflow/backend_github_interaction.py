```python
import requests
from backend.github_api import GitHubAPI

serverUrl = "http://localhost:5000"

def sendRequest(message, data):
    response = requests.post(f"{serverUrl}/{message}", json=data)
    return response.json()

def handleGitHubInteraction(message, data):
    if message == "generateCode":
        return GitHubAPI.generate_code(data)
    elif message == "manageRepo":
        return GitHubAPI.manage_repository(data)
    else:
        return {"error": "Invalid message"}

def processRequest(request):
    message = request.get("message")
    data = request.get("data")
    response = handleGitHubInteraction(message, data)
    return sendRequest("response", response)
```