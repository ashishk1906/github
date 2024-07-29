# Github Issue Fetcher

Github Issue Fetcher is a Python tool that interacts with the GitHub API to fetch, process, and export issues from a specified GitHub repository.
It provides a straightforward way to retrieve issue data, save it in JSON format, and convert it into CSV for further analysis.

## Project Overview

This project is designed to help developers and data analysts easily access and manage GitHub issue data. 
It offers a simple command-line interface to fetch the latest issues from a GitHub repository and provides functionalities to save the issues as a JSON file and convert them to a CSV format. 

## Requirements

- Python 3.6 or later
- `requests` library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/quadratic404/github-issue-fetcher.git
    cd github-issue-fetcher
    ```

2. Install the package:
    ```sh
    pip install .
    ```

## Usage

1. Set the `GITHUB_TOKEN` environment variable with your GitHub token.

    ### On Windows (Command Prompt):
    ```sh
    set GITHUB_TOKEN=your_actual_github_token_here
    ```

    ### On Windows (PowerShell):
    ```sh
    $env:GITHUB_TOKEN="your_actual_github_token_here"
    ```

    ### On macOS/Linux:
    ```sh
    export GITHUB_TOKEN=your_actual_github_token_here
    ```

2. Run the client application:
    ```sh
    python client.py
    ```

This will prompt you to enter the number of issues to fetch from the `kubernetes/kubernetes` repository, save them as a JSON file (`kubernetes_issues.json`), and convert them into a CSV file (`kubernetes_issues.csv`).

## Running the Application

### Using Python Script

1. Open a terminal or command prompt.
2. Navigate to the directory containing `client.py`.
3. Run the script using the command:
    ```sh
    python client.py
    ```

### Using Console Entry Point

1. Ensure you have installed the package as described in the installation section.
2. Run the script using the console entry point:
    ```sh
    github_issue_fetcher
    ```

## Functionality

- The script will prompt you to enter the number of issues you want to fetch.
- It supports fetching more than 100 issues by making multiple requests to the GitHub API, as the API has a limit of fetching 100 issues per request.

## File Descriptions

- `client.py`: Main script that fetches issues, saves them as JSON, processes the issues, and converts them to CSV.
- `__init__.py`: Initialization file for the `issue_manager` package.
- `fetch_issues.py`: Contains functions to fetch issues from the GitHub API and save them as JSON.
- `process_issues.py`: Contains functions to process issues and identify relevant fields.
- `convert_issues.py`: Contains functions to convert the processed issues to a CSV file.
- `setup.py`: Setup script for packaging the project.

## Notes

- Ensure you have a stable internet connection while running the script.
- Set the `GITHUB_TOKEN` environment variable with a valid token to avoid authorization issues.
- The script will prompt for the number of issues to fetch and can handle requests exceeding 100 issues by making multiple API calls.
