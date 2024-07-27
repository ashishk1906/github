import csv

def convert_issues_to_csv(issues, csv_file_path):
    with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['issue_number', 'issue_title', 'issue_url', 'issue_created_date', 'issue_state', 'issue_user', 'issue_labels'])
        
        for issue in issues:
            writer.writerow([
                issue['issue_number'],
                issue['issue_title'],
                issue['issue_url'],
                issue['issue_created_date'],
                issue['issue_state'],
                issue['issue_user'],
                issue['issue_labels'],
            ])
    
    print(f"CSV file '{csv_file_path}' has been created successfully.")
