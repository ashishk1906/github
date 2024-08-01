import os
from issue_manager.fetch_issues import fetch_issues, save_data_as_json
from issue_manager.process_issues import identify_relevant_fields
from issue_manager.convert_issues import convert_issues_to_csv

def client_app():
    token = os.getenv('GITHUB_TOKEN')  # Read GitHub token from environment variable
    if not token:
        raise ValueError("Please set the GITHUB_TOKEN environment variable")
    
    repo_owner = input("Enter the repository owner: ")
    repo_name = input("Enter the repository name: ")
    
    choice = input("Do you want to fetch issues by range (r) or latest N issues (l)? (Enter 'r' or 'l'): ").strip().lower()
    
    if choice == 'r':
        start_issue_number = int(input("Enter the start issue number: "))
        end_issue_number = int(input("Enter the end issue number: "))
        try:
            issues = fetch_issues(token, repo_owner, repo_name, start_issue_number=start_issue_number, end_issue_number=end_issue_number)
        except ValueError as e:
            print(e)
            return
    elif choice == 'l':
        num_issues = int(input("Enter the number of latest issues to fetch: "))
        try:
            issues = fetch_issues(token, repo_owner, repo_name, num_issues=num_issues)
        except ValueError as e:
            print(e)
            return
    else:
        print("Invalid choice. Please enter 'r' or 'l'.")
        return
    
    if not issues:
        print("No issues found or there was an error fetching the issues.")
        return
    
    # Define file paths
    json_file_path = f'{repo_name}_issues.json'
    csv_file_path = f'{repo_name}_issues.csv'
    
    # Save issues as JSON
    save_data_as_json(issues, json_file_path)
    
    # Identify relevant fields
    relevant_issues = identify_relevant_fields(issues)
    
    # Convert issues to CSV
    convert_issues_to_csv(relevant_issues, csv_file_path)
    
    print(f"JSON file '{json_file_path}' has been created successfully.")
    print(f"CSV file '{csv_file_path}' has been created successfully.")

if __name__ == "__main__":
    client_app()
