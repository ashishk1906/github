import requests
import json

def fetch_issues(token, repo_owner, repo_name, num_issues):
    headers = {'Authorization': f'token {token}'}
    issues = []
    page = 1
    per_page = 100

    while len(issues) < num_issues:
        remaining_issues = num_issues - len(issues)
        per_page = min(remaining_issues, per_page)
        
        url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/issues'
        params = {'state': 'open', 'per_page': per_page, 'page': page, 'sort': 'created', 'direction': 'desc'}
        
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        
        fetched_issues = response.json()
        if not fetched_issues:
            break
        
        issues.extend(fetched_issues)
        page += 1

    return issues[:num_issues]

def save_issues_as_json(issues, file_path):
    with open(file_path, 'w') as f:
        json.dump(issues, f, indent=2)
