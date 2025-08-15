# 🚀 AutoPost: Cronify Your Content

**AutoPost** is a powerful automation tool that brings life to your LinkedIn profile, without you lifting a finger. Using GitHub Actions, it schedules and publishes dynamic, human-like posts directly to LinkedIn and Twitter. The magic? It runs hourly at `:47` (because no human posts on the hour, right?) and picks two random hours daily for actual LinkedIn content. All other times, your thoughts go to Twitter. Genius? Slightly.

---

## ✨ Features

* ✅ **Human-Like Posting Times**: Runs hourly at `:47` and posts **twice a day** to LinkedIn at random hours (within 10 AM to 10 PM IST).
* ✅ **Fallback to Twitter**: Every other run posts to Twitter instead, keeping your brand alive and buzzing across platforms.
* ✅ **OAuth2 Authentication**: Secure LinkedIn API integration.
* ✅ **AI-Powered Content Generation**: Uses a custom prompt to generate text via the Gemini API.
* ✅ **Seamless Automation**: Managed fully by GitHub Actions; set it and forget it.

---

## ⏰ How It Works

1. **Hourly Cron**: A GitHub Actions workflow runs every hour at `:47` UTC.
2. **Smart Random Logic**:

   * **2 out of 12 runs per day** (randomized) are selected to post on LinkedIn.
   * **Other 10 runs** default to Twitter.
3. **AI Content**: A Google Gemini model (via API key) is queried with your custom `PROMPT` or `PROMPT_X` to generate platform-specific posts.
4. **LinkedIn Posts**:

   * Posted via the `ugcPosts` endpoint using your personal URN.
   * Public visibility.
5. **Twitter Posts**:

   * Posted via Twitter API v2 using Tweepy.

---

## 🛠️ Prerequisites

Before you deploy, make sure you have:

* Python 3.12+
* A LinkedIn Developer App with access token generation enabled
* A Twitter Developer App with API v2 access
* A GitHub repository
* GitHub Actions enabled

---

## 🔑 Required Secrets

Set these in your GitHub repository's **Settings > Secrets and variables > Actions**:

| Secret Name              | Description                                |
| ------------------------ | ------------------------------------------ |
| `GOOGLE_API_KEY`         | Gemini AI API key (for content generation) |
| `LINKEDIN_ACCESS_TOKEN`  | LinkedIn OAuth2 access token               |
| `LINKEDIN_CLIENT_ID`     | LinkedIn App client ID                     |
| `LINKEDIN_CLIENT_SECRET` | LinkedIn App client secret                 |
| `PROMPT`                 | Prompt for LinkedIn post generation        |
| `PROMPT_X`               | Prompt for Twitter post generation         |
| `X_BEARER_TOKEN`         | Twitter API bearer token                   |
| `X_API_KEY`              | Twitter API key                            |
| `X_API_SECRET`           | Twitter API secret                         |
| `X_ACCESS_TOKEN`         | Twitter access token                       |
| `X_ACCESS_SECRET`        | Twitter access token secret                |
| `NOTIFICATION_EMAIL`     | Optional: Email for notifications          |

---

## 📦 Installation

1. Clone the repo:

```bash
git clone https://github.com/yourusername/LinkedIn-AutoPost.git
cd LinkedIn-AutoPost
```

2. Set your GitHub Secrets as described above.
3. Ensure the `.github/workflows/main.yml` is present and set to run every hour at `:47`.

```yaml
schedule:
  - cron: '47 * * * *'
```

4. Push and let GitHub Actions take over.

---

## 🧠 Logic Behind the Scenes

* `main.py` contains the decision tree:

  * Every hour it checks if it's one of the 2 lucky LinkedIn posting hours.
  * If yes, it posts to LinkedIn using Gemini-generated content.
  * If not, it posts to Twitter using a separate prompt and set of API keys.

This mimics natural, non-robotic behavior; perfect for building trust with your audience.

---

## 📧 Notifications (Optional)

You can optionally integrate Gmail or other services using the `NOTIFICATION_EMAIL` secret for updates after each post. This is currently a placeholder for future extensions.

---

## 🛡️ Security

* All tokens and secrets are stored in **GitHub Secrets**.
* Avoid hardcoding credentials.
* Logs only show non-sensitive data.

---

## 🌿 Future Improvements

* [ ] Image + media support
* [ ] Auto-refresh for expired LinkedIn tokens
* [ ] Enhanced scheduling UI via GitHub Actions Dispatch
* [ ] Email summaries of posts made
* [ ] Post analytics

---

## 💬 Sample AI Prompts

**LinkedIn Prompt** (`PROMPT`):

```
Write a professional, yet engaging post on emerging AI trends in 2025 for a tech-savvy audience.
```

**Twitter Prompt** (`PROMPT_X`):

```
Tweet a witty and insightful one-liner about how AI is rewriting the rules of productivity in 2025.
```

---

## 🔁 Manual Trigger

Want to test manually? Go to **GitHub > Actions > Run workflow** and manually trigger the cron workflow.

---

## 🧠 Philosophy

> "Even bots need a personal brand."

This project doesn’t just automate posts; it mimics the unpredictability and style of human behavior. Build trust. Stay active. And do it while you sleep.

---

## 🤖 Author

**Built with ❤️ by [Satwik Bhusanur](https://github.com/voidconsole)**
