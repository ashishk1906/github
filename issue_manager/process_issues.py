def identify_relevant_fields(issues):
    relevant_issues = []
    for issue in issues:
        relevant_issue = {
            'issue_number': issue['number'],
            'issue_title': issue['title'],
            'issue_url': issue['html_url'],
            'issue_created_date': issue['created_at'],
            'issue_state': issue['state'],
            'issue_user': issue['user']['login'],
            'issue_labels': ', '.join(label['name'] for label in issue['labels']),
        }
        relevant_issues.append(relevant_issue)
    return relevant_issues
