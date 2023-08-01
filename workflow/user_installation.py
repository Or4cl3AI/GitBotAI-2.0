import requests
from github import Github

def install_gitbotai(user_token, repo_name):
    """
    Function to install GitBotAI as a GitHub app on user's repositories.
    """
    # Initialize a Github instance with user's token
    g = Github(user_token)

    try:
        # Get user's repository
        repo = g.get_user().get_repo(repo_name)

        # Define the headers for the installation request
        headers = {
            'Accept': 'application/vnd.github.machine-man-preview+json',
            'Authorization': f'token {user_token}'
        }

        # Define the payload for the installation request
        payload = {
            'repository_ids': [repo.id]
        }

        # Send a POST request to install the GitBotAI app
        response = requests.post('https://api.github.com/app/installations', headers=headers, json=payload)

        # Check if the installation was successful
        if response.status_code == 201:
            print(f'GitBotAI has been successfully installed on the repository: {repo_name}')
        else:
            print(f'Failed to install GitBotAI on the repository: {repo_name}. Please check your token and repository name.')

    except Exception as e:
        print(f'An error occurred: {str(e)}')
