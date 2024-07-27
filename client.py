from Issue_Manager.fetch_issues import fetch_issues, save_issues_as_json
from Issue_Manager.process_issues import identify_relevant_fields
from Issue_Manager.convert_issues import convert_issues_to_csv

def client_app():
    token = '123'  # Replace with your actual GitHub token
    repo_owner = 'kubernetes'
    repo_name = 'kubernetes'
    num_issues = 10
    
    # Fetch issues
    issues = fetch_issues(token, repo_owner, repo_name, num_issues)
    
    # Define file paths
    json_file_path = 'kubernetes_issues.json'
    csv_file_path = 'kubernetes_issues.csv'
    
    # Save issues as JSON
    save_issues_as_json(issues, json_file_path)
    
    # Identify relevant fields
    relevant_issues = identify_relevant_fields(issues)
    
    # Convert issues to CSV
    convert_issues_to_csv(relevant_issues, csv_file_path)

if __name__ == "__main__":
    client_app()

 