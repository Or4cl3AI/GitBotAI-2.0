import requests
from flask import jsonify
from marshmallow import Schema, fields

# Define the data schemas
class UserSchema(Schema):
    id = fields.Int(required=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)

class RepoSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    owner = fields.Nested(UserSchema, required=True)

# Define the GitHub API class
class GitHubAPI:
    BASE_URL = "https://api.github.com"

    def __init__(self, access_token):
        self.headers = {
            "Authorization": f"Bearer {access_token}",
            "Accept": "application/vnd.github.v3+json"
        }

    def get_user(self, username):
        response = requests.get(f"{self.BASE_URL}/users/{username}", headers=self.headers)
        return UserSchema().load(response.json())

    def get_repo(self, owner, repo):
        response = requests.get(f"{self.BASE_URL}/repos/{owner}/{repo}", headers=self.headers)
        return RepoSchema().load(response.json())

    def create_repo(self, name, description="", private=False):
        data = {
            "name": name,
            "description": description,
            "private": private
        }
        response = requests.post(f"{self.BASE_URL}/user/repos", headers=self.headers, json=data)
        return RepoSchema().load(response.json())

    def delete_repo(self, owner, repo):
        response = requests.delete(f"{self.BASE_URL}/repos/{owner}/{repo}", headers=self.headers)
        return response.status_code == 204