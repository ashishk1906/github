import os
from issue_manager.fetch_issues import fetch_issues, save_issues_as_json
from issue_manager.process_issues import identify_relevant_fields
from issue_manager.convert_issues import convert_issues_to_csv

def client_app(num_issues):
    token = os.getenv('GITHUB_TOKEN')  # Read GitHub token from environment variable
    if not token:
        raise ValueError("Please set the GITHUB_TOKEN environment variable")
    
    repo_owner = 'kubernetes'
    repo_name = 'kubernetes'
    
    # Fetch issues
    issues = fetch_issues(token, repo_owner, repo_name, num_issues)
    
    # Define file paths
    json_file_path = 'kubernetes_issues.json'
    csv_file_path = 'kubernetes_issues.csv'
    
    # Save issues as JSON
    save_issues_as_json(issues, json_file_path)
    print(f"JSON file '{json_file_path}' has been created successfully.")
    
    # Identify relevant fields
    relevant_issues = identify_relevant_fields(issues)
    
    # Convert issues to CSV
    convert_issues_to_csv(relevant_issues, csv_file_path)
    print(f"CSV file '{csv_file_path}' has been created successfully.")

if __name__ == "__main__":
    # Get user input for the number of issues
    num_issues = int(input("Enter the number of issues to fetch: "))

    # Run the application
    client_app(num_issues)
