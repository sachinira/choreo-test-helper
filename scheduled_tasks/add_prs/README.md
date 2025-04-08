# GitHub PR Tracker

This scheduled task fetches all Pull Requests created by you from GitHub and updates a Google Sheet with the details.

## Prerequisites

1. GitHub Personal Access Token
   - Go to GitHub Settings > Developer Settings > Personal Access Tokens
   - Create a new token with `repo` scope
   - Copy the token

2. Google Sheets Setup
   - Create a new Google Sheet
   - Enable Google Sheets API in Google Cloud Console
   - Create a service account and download the credentials JSON file
   - Share the Google Sheet with the service account email

## Configuration

1. In Choreo, create a new scheduled task and upload this code
2. Configure the following environment variables:
   - `githubToken`: Your GitHub Personal Access Token
   - `googleSheetsCredentials`: The contents of your Google Sheets service account credentials JSON file
   - `spreadsheetId`: The ID of your Google Sheet (found in the URL)
   - `sheetName`: The name of the sheet to update (default: "PRs")

## Schedule

The task runs daily at midnight (0 0 * * *). You can modify the schedule in the `@schedule:Schedule` annotation in `github_pr_tracker.bal`.

## Output

The Google Sheet will be updated with the following columns:
- Title
- Repository
- URL
- State
- Created At
- Updated At 