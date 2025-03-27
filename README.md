# 🚀 LinkedIn AutoPost: Cronify Your Content

LinkedIn AutoPost is a powerful automation tool that randomly schedules and posts content on your LinkedIn profile using GitHub Actions. It generates dynamic cron jobs to ensure unpredictable and authentic-looking post timings.

## ✨ Features
- ✅ **Randomized Scheduling**: Posts twice daily at unpredictable times within a 10 AM to 10 PM IST window.
- ✅ **OAuth2 Authentication**: Secure LinkedIn API integration.
- ✅ **Automated Content Posting**: Post directly to LinkedIn using your personalized prompts.
- ✅ **Seamless Integration**: Managed entirely through GitHub Actions.

## 🛠️ Prerequisites
Ensure you have the following set up:
- Python 3.12
- LinkedIn Developer Account with API access
- GitHub Repository
- GitHub Secrets for storing API credentials

## 🔑 Environment Variables
Set the following secrets in your repository:
- `GOOGLE_API_KEY` — For any external AI services (if applicable)
- `LINKEDIN_ACCESS_TOKEN` — Your LinkedIn access token
- `LINKEDIN_CLIENT_ID` — Your LinkedIn client ID
- `LINKEDIN_CLIENT_SECRET` — Your LinkedIn client secret
- `PROMPT` — Custom prompt for generating content
- `NOTIFICATION_EMAIL` — Email for notifications

## 🚦 How It Works
1. **Random Cron Generation**: The workflow uses a Bash script to generate random UTC times between 4 AM and 4 PM (matching your 10 AM to 10 PM IST window).
2. **GitHub Actions**: Commits and updates the `.github/workflows/main.yml` with new cron jobs.
3. **LinkedIn API Call**: Executes the `main.py` script to generate and post content.

## 🚀 Running the Workflow
- To trigger the workflow manually, navigate to your GitHub Actions tab and click **Run Workflow**.
- To schedule automatically, the cron will handle it at the generated times.

## 📧 Notifications
You can receive email notifications about your posts using the `NOTIFICATION_EMAIL` secret. Alternatively, you could expand this by integrating Gmail or other notification services.

## 🛡️ Security
- Store all sensitive information in GitHub Secrets.
- Avoid storing API keys directly in your code.

## 🌿 Future Improvements
- Add AI-powered content generation.
- Support for multiple LinkedIn accounts.
- Improved logging and error handling.

---
**LinkedIn AutoPost - Because even bots need a personal brand.**
