import ballerinax/github;
import ballerinax/persist.googlesheets;
import ballerina/time;

// Configuration for GitHub and Google Sheets
configurable string githubToken = ?;
configurable string googleSheetsCredentials = ?;
configurable string spreadsheetId = ?;
configurable string sheetName = "PRs";

// Initialize GitHub client
final github:Client githubClient = check new ({
    auth: {
        token: githubToken
    }
});

// Initialize Google Sheets client
final googlesheets:Client sheetsClient = check new ({
    auth: {
        credentials: googleSheetsCredentials
    }
});

// Function to get all PRs created by the authenticated user
function getMyPRs() returns github:PullRequest[]|error {
    // Get the authenticated user's PRs
    github:PullRequest[] prs = check githubClient->/search/issues.get({
        q: "is:pr author:@me",
        sort: "created",
        order: "desc"
    }).items;
    return prs;
}

// Function to update Google Sheet with PR data
function updateGoogleSheet(github:PullRequest[] prs) returns error? {
    // Prepare data for the sheet
    var sheetData = from var pr in prs
        select {
            "Title": pr.title,
            "Repository": pr.repository.full_name,
            "URL": pr.html_url,
            "State": pr.state,
            "Created At": pr.created_at,
            "Updated At": pr.updated_at
        };

    // Update the Google Sheet
    check sheetsClient->/spreadsheets/{spreadsheetId}/values/{sheetName}!A1:append.post({
        valueInputOption: "USER_ENTERED",
        insertDataOption: "INSERT_ROWS",
        values: sheetData
    });
}

// Scheduled task that runs daily
@schedule:Schedule {
    cron: "0 0 * * *"  // Runs at midnight every day
}
function runPRTracker() {
    // Get PRs
    github:PullRequest[]|error prs = getMyPRs();
    if prs is error {
        log:printError("Error fetching PRs", prs);
        return;
    }

    // Update Google Sheet
    error? result = updateGoogleSheet(prs);
    if result is error {
        log:printError("Error updating Google Sheet", result);
        return;
    }

    log:printInfo("Successfully updated PRs in Google Sheet");
} 