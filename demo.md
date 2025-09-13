# Preview
https://github.com/user-attachments/assets/6f814d56-9ff2-4623-ade9-7662495acb43

# To use the automation
If you read the [readme.md](https://github.com/voidconsole/autopost/tree/6c31a7472e37f99e4806f71f7ea4f6d156915286) (and do read it :P), it should be pretty clear. Just fork the repo, get the API keys, put them in the Settings > Secrets and Variables > Actions. Tweak the parameters of the code if you wish. 
And that's pretty much it, just wait for the magic to happen, or run it yourself manually in Actions > Post > Run Workflow.

# To set the API keys
Now this is a one time effort to set up the automation, and you need to set-up the following accounts and keys(free!):
Don't worry, since this happens in your personal github, no one but you can see and set them.

| Secret Name              | Description                                | How to get it
| ------------------------ | ------------------------------------------ | -------------------------------------------------------------------------------------------------------
| `GOOGLE_API_KEY`         | Gemini AI API key (for content generation) | Create a new Google Cloud project, go to Google AI studio, and create a Gemini API KEY for that project.
| `LINKEDIN_CLIENT_ID`     | LinkedIn App client ID                     | Create a new Linkedin Developer profile, create a new App (Use the details for your account page, or set up a new one), and after completion, add "Share on linkedin" and "OpenID Connect" in the Products. After verification, in the Auth tab, get the Client ID, and Client Secret below it.
| `LINKEDIN_CLIENT_SECRET` | LinkedIn App client secret                 | This was recieved in the above step itself. 
| `LINKEDIN_ACCESS_TOKEN`  | LinkedIn OAuth2 access token               | To get the access token, follow https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow upto the 3rd step. Or, https://learn.microsoft.com/en-us/linkedin/shared/authentication/postman-getting-started if you want to use Postman. IMPORTANT thing is, the scopes you set in both the links, must be `openid`, `profile`, `email` and `w_member_social`.  
| `PROMPT`                 | Prompt for LinkedIn post generation        | You can set this to whatever you like. Although, a well-defined descriptive prompt works best.
| `PROMPT_X`               | Prompt for Twitter post generation         | You can set this to whatever you like. Although, a well-defined descriptive prompt works best.
| `X_BEARER_TOKEN`         | Twitter API bearer token                   | Create a X API Developer Account, create a new project, for X API v1.1 and in authenication settings, select "Read and Write" and "Web App/Automation Bot". After it's done, find the Bearer token in "Tokens and Keys" tab of your project.  
| `X_API_KEY`              | Twitter API key                            | Just as in last step, find it in "Keys and Tokens".
| `X_API_SECRET`           | Twitter API secret                         | Just as in last step, find it in "Keys and Tokens".
| `X_ACCESS_TOKEN`         | Twitter access token                       | Just as in last step, find it in "Keys and Tokens".
| `X_ACCESS_SECRET`        | Twitter access token secret                | Just as in last step, find it in "Keys and Tokens".

Once you set this, you're good to go! Watch the automation grow your profile by posting consistently, written to your will. 
