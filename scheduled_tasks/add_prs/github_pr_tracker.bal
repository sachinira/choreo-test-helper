import ballerinax/trigger.github;
import ballerinax/googleapis.sheets as sheets;
import ballerina/log;
import ballerina/http;

// Configuration for GitHub and Google Sheets
type OAuth2RefreshTokenGrantConfig record {
    string clientId;
    string clientSecret;
    string refreshToken;
    string refreshUrl = "https://www.googleapis.com/oauth2/v3/token";
};

configurable github:ListenerConfig gitHubListenerConfig = ?; 

listener http:Listener httpListener = check new(8090);
listener github:Listener webhookListener = new(gitHubListenerConfig, httpListener);

configurable OAuth2RefreshTokenGrantConfig sheetOauthConfig = ?;
configurable string spreadsheetId = ?;
configurable string worksheetName = ?;

// Spreadsheet header constants
final string[] & readonly headerValues = [
    "Commit Author Name",
    "Commit Author Email",
    "Commit Message",
    "Commit URL",
    "Repository Name",
    "Repository URL"
];

const int HEADINGS_ROW = 1;

@display { label: "GitHub New PR to Google Sheets Row" }
service github:PushService on webhookListener {
    remote function onPush(github:PushEvent payload) returns error? {
      sheets:Client spreadsheetClient = check new ({auth: {
            clientId: sheetOauthConfig.clientId,
            clientSecret: sheetOauthConfig.clientSecret,
            refreshToken: sheetOauthConfig.refreshToken,
            refreshUrl: sheetOauthConfig.refreshUrl            
        }});

        sheets:Row headers = check spreadsheetClient->getRow(spreadsheetId, worksheetName, HEADINGS_ROW);
        if headers.values.length() == 0 {
            check spreadsheetClient->appendRowToSheet(spreadsheetId, worksheetName, headerValues);
        }

        foreach var item in payload.commits {
            (int|string|decimal)[] values = [item.author.name, item.author.email, item.message, item.url, payload.repository.name, payload.repository.url];
            check spreadsheetClient->appendRowToSheet(spreadsheetId, worksheetName, values);
        }
        log:printInfo("Github new PR appended successfully!");
    }
}

service /ignore on httpListener {}