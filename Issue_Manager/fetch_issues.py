import requests
import json

def fetch_issues(token, repo_owner, repo_name, num_issues=10):
    url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/issues'
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    params = {
        'state': 'open',
        'per_page': num_issues,
        'sort': 'created',
        'direction': 'desc'
    }

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()  # Raise an exception for HTTP errors

    issues = response.json()
    return issues

def save_issues_as_json(issues, file_path):
    with open(file_path, 'w') as file:
        json.dump(issues, file, indent=2)
    print(f"JSON file '{file_path}' has been created successfully.")
