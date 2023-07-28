```python
import json

def handleResponse(response):
    """
    Function to handle responses from the backend server
    """
    # Parse the JSON response
    data = json.loads(response)

    # Check if the response contains an 'error' key
    if 'error' in data:
        print(f"Error: {data['error']}")
        return

    # Handle different types of responses
    if 'generateCode' in data:
        print(f"Generated code: {data['generateCode']}")
    elif 'manageRepo' in data:
        print(f"Repository management status: {data['manageRepo']}")
    else:
        print("Unknown response from the server")

    return data
```