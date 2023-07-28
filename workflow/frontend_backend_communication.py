```python
import requests

# Shared variables
serverUrl = "http://localhost:5000/api"
iframeSrc = "https://ora.ai/embed/2016a484-b6bd-446f-9061-16fc900331b5"
chatbotIframe = "chatbotIframe"
actionButton = "actionButton"

# Message names
generateCode = "generateCode"
manageRepo = "manageRepo"

def sendRequest(url, data):
    response = requests.post(url, json=data)
    return response.json()

def handleResponse(response):
    if response.status_code == 200:
        print("Request successful.")
    else:
        print("Request failed.")

def frontend_backend_communication():
    # User interacts with the conversational interface or triggers an action in the UI
    userAction = input("Enter your action: ")

    if userAction == generateCode:
        # Send a request to the backend server to generate code
        response = sendRequest(serverUrl + "/generateCode", {"iframeSrc": iframeSrc})
        handleResponse(response)
    elif userAction == manageRepo:
        # Send a request to the backend server to manage repository
        response = sendRequest(serverUrl + "/manageRepo", {"iframeSrc": iframeSrc})
        handleResponse(response)
    else:
        print("Invalid action.")

if __name__ == "__main__":
    frontend_backend_communication()
```