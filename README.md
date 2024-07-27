
## Requirements

-  Python 3.6 or later
- `requests` library

## Installation

1. Clone the repository:
    ```
    git clone https://github.com/yourusername/github_issues_fetcher.git
    cd github_issues_fetcher
    ```

2. Install the package:
    ```
    pip install .
    ```

## Usage

1. Replace the placeholder `your_github_token_here` in `client.py` with your actual GitHub token.

2. Run the client application:
    ```
    github_issue_fetcher
    ```

This will fetch the latest 10 issues from the `kubernetes/kubernetes` repository, save them as a JSON file (`kubernetes_issues.json`), and convert them into a CSV file (`kubernetes_issues.csv`).

## Running the Application

### Using Python Script

1. Open a terminal or command prompt.
2. Navigate to the directory containing `client.py`.
3. Run the script using the command:
    ```
    python client.py
    ```

### Using Console Entry Point

1. Ensure you have installed the package as described in the setup section.
2. Run the script using the console entry point:
    ```
   github_issue_fetcher
    ```

## File Descriptions

- `client.py`: Main script that fetches issues, saves them as JSON, processes the issues, and converts them to CSV.
- `__init__.py`: Initialization file for the `issue_manager` package.
- `fetch_issues.py`: Contains functions to fetch issues from the GitHub API and save them as JSON.
- `process_issues.py`: Contains functions to process issues and identify relevant fields.
- `convert_issues.py`: Contains functions to convert the processed issues to a CSV file.
- `setup.py`: Setup script for packaging the project.

## Notes

- Ensure you have a stable internet connection while running the script.
- Replace the placeholder GitHub token in `client.py` with a valid token to avoid authorization issues.
