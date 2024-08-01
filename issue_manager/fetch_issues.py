import requests
import json

def fetch_issues(token, repo_owner, repo_name, start_issue_number=None, end_issue_number=None, num_issues=None):
    headers = {'Authorization': f'token {token}'}
    issues = []
    page = 1
    per_page = 100

    try:
        while True:
            url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/issues'
            params = {'state': 'all', 'per_page': per_page, 'page': page, 'sort': 'created', 'direction': 'desc' if num_issues else 'asc'}
            
            response = requests.get(url, headers=headers, params=params)
            
            # Check for HTTP errors
            response.raise_for_status()
            
            # Check for GitHub API error in response
            if response.status_code == 401:
                raise ValueError("Invalid GitHub token. Please check your token and try again.")
            
            fetched_issues = response.json()
            if not fetched_issues:
                break
            
            if start_issue_number is not None and end_issue_number is not None:
                for issue in fetched_issues:
                    issue_number = issue['number']
                    if start_issue_number <= issue_number <= end_issue_number:
                        issues.append(issue)
                    elif issue_number > end_issue_number:
                        return issues
            else:
                issues.extend(fetched_issues[:num_issues])
                if len(issues) >= num_issues:
                    return issues[:num_issues]
            
            page += 1

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    
    return issues

def save_data_as_json(data, file_path):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)
