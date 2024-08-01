# Github Issue Fetcher

Github Issue Fetcher is a Python tool that interacts with the GitHub API to fetch, process, and export issues from a specified GitHub repository. It provides a straightforward way to retrieve issue data, save it in JSON format, and convert it into CSV for further analysis.

## Project Overview

This project is designed to help developers and data analysts easily access and manage GitHub issue data. It offers a simple way to fetch issues from a GitHub repository by specifying either a range of issue numbers or retrieving the latest issues. The tool saves the issues as a JSON file and converts them into a CSV format for further analysis.

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

    The application will prompt you for the following inputs:
    - **Repository Owner**: Enter the owner of the GitHub repository.
    - **Repository Name**: Enter the name of the GitHub repository.
    - **Fetch Mode**: Choose whether to fetch issues by range (`r`) or by latest issues (`l`).

    ### Fetch by Range (`r`)
    If you choose to fetch issues by range, you will be prompted to enter:
    - **Start Issue Number**: Enter the starting issue number for the range.
    - **End Issue Number**: Enter the ending issue number for the range.

    ### Fetch Latest Issues (`l`)
    If you choose to fetch the latest issues, you will be prompted to enter:
    - **Number of Latest Issues**: Enter the number of the latest issues you want to fetch.

    After fetching the issues, the tool will save them as a JSON file (e.g., `kubernetes_issues.json`) and convert them into a CSV file (e.g., `kubernetes_issues.csv`).

## Running the Application

1. Open a terminal or command prompt.
2. Navigate to the directory containing `client.py`.
3. Run the script using the command:
    ```sh
    python client.py
    ```

## Functionality

- **Fetching Issues**: The script allows you to fetch issues from a GitHub repository either by specifying a range of issue numbers or retrieving the latest issues.
- **Handling Invalid Tokens**: The script will notify you if the provided GitHub token is invalid.
- **Multiple Requests**: Supports fetching more than 100 issues by making multiple requests to the GitHub API, as the API has a limit of fetching 100 issues per request.

## File Descriptions

- `client.py`: Main script that interacts with the GitHub API, fetches issues, processes them, and converts them to JSON and CSV formats.
- `__init__.py`: Initialization file for the `issue_manager` package.
- `fetch_issues.py`: Contains functions to fetch issues from the GitHub API and save them as JSON.
- `process_issues.py`: Contains functions to process issues and identify relevant fields.
- `convert_issues.py`: Contains functions to convert the processed issues to a CSV file.
- `setup.py`: Setup script for packaging the project.

## Notes

- Ensure you have a stable internet connection while running the script.
- Set the `GITHUB_TOKEN` environment variable with a valid token to avoid authorization issues.
- The script can handle requests exceeding 100 issues by making multiple API calls.
