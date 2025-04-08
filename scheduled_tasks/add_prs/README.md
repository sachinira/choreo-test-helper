# GitHub PR Tracker

A Ballerina service that automatically tracks GitHub push events and records commit information in a Google Sheets spreadsheet.

## Overview

This service listens for GitHub push events and automatically logs commit details including:
- Commit author name
- Commit author email
- Commit message
- Commit URL
- Repository name
- Repository URL

The data is stored in a configured Google Sheets spreadsheet for easy tracking and analysis.

## Prerequisites

- Ballerina 2201.7.4 or higher
- GitHub webhook configuration
- Google Sheets API access
- Google OAuth2 credentials

## Configuration

The service requires the following configurations:

### GitHub Configuration
```toml
[gitHubListenerConfig]
# GitHub webhook configuration
```

### Google Sheets Configuration
```toml
[sheetOauthConfig]
clientId = "<your-client-id>"
clientSecret = "<your-client-secret>"
refreshToken = "<your-refresh-token>"

spreadsheetId = "<your-spreadsheet-id>"
worksheetName = "<your-worksheet-name>"
```

## Features

- Automatic header creation if the spreadsheet is empty
- Logs multiple commits from a single push event
- Error handling and logging
- Runs on port 8090

## Development

1. Update the configuration values in `Config.toml`
2. Run the service:
   ```bash
   bal run
   ```

## License

This project is licensed under the terms specified in the repository's main LICENSE file.
