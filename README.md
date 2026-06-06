# AutoPost

A weird little automation project that lets AI run your social media accounts.

This started as an experiment with GitHub Actions, LinkedIn APIs, prompt engineering, and posting behavior. The system runs entirely in the cloud and automatically generates + publishes content to LinkedIn and Twitter/X without any manual interaction.

It was mainly built to answer a question:

> Can AI convincingly fake an active intellectual online presence?

Turns out: not really.

But the infrastructure was fun to build.

---

# What It Does

* Runs hourly using GitHub Actions
* Executes at `:47` every hour because posting exactly on the hour looks robotic
* Randomly selects 2 posting slots per day for LinkedIn
* All remaining runs post to Twitter/X
* Generates content using Gemini
* Uses different prompts for LinkedIn and Twitter
* Posts automatically through platform APIs

Once configured, it just keeps running.

---

# Stack

* Python
* GitHub Actions
* Google Gemini API
* LinkedIn API
* Twitter/X API v2
* Tweepy

---

# How The Scheduling Works

The GitHub Actions workflow runs every hour:

```yaml
schedule:
  - cron: '47 * * * *'
```

Each run checks whether the current hour is one of the randomly selected LinkedIn slots for that day.

* If yes → generate and publish a LinkedIn post
* If not → generate and publish a Twitter/X post

The randomization exists purely to avoid obvious automation patterns.

---

# Prompt Engineering

The prompts ended up becoming more complicated than the actual infrastructure.

The system uses:

* tone constraints
* formatting instructions
* topic control
* hook structures
* CTA patterns
* platform-specific writing styles

LinkedIn and Twitter use completely separate prompts.

The goal was to make the generated posts sound:

* human,
* slightly intellectual,
* platform-native,
* and not obviously AI-generated.

It partially worked.

---

# Requirements

Before running this project, you'll need:

* Python 3.12+
* GitHub Actions enabled
* A LinkedIn developer app
* A Twitter/X developer app
* Gemini API access

---

# Required GitHub Secrets

Set these under:

`Settings → Secrets and variables → Actions`

| Secret                   | Purpose                     |
| ------------------------ | --------------------------- |
| `GOOGLE_API_KEY`         | Gemini API key              |
| `LINKEDIN_ACCESS_TOKEN`  | LinkedIn OAuth token        |
| `LINKEDIN_CLIENT_ID`     | LinkedIn app client ID      |
| `LINKEDIN_CLIENT_SECRET` | LinkedIn app client secret  |
| `PROMPT`                 | LinkedIn generation prompt  |
| `PROMPT_X`               | Twitter/X generation prompt |
| `X_BEARER_TOKEN`         | Twitter/X bearer token      |
| `X_API_KEY`              | Twitter/X API key           |
| `X_API_SECRET`           | Twitter/X API secret        |
| `X_ACCESS_TOKEN`         | Twitter/X access token      |
| `X_ACCESS_SECRET`        | Twitter/X access secret     |

---

# Setup

Clone the repo:

```bash
git clone https://github.com/voidconsole/autopost.git
cd autopost
```

Configure all required GitHub Secrets.

Then push the workflow and let GitHub Actions handle the rest.

---

# Notes

LinkedIn API setup is painful.

You will create:

* too many tokens,
* too many apps,
* too many permissions,
* and probably question your life choices at least once.

Also:
LinkedIn access tokens expire, so eventually this thing breaks unless refreshed manually.

---

# Future Ideas

* Media/image support
* Token auto-refresh
* Analytics dashboard
* Better scheduling controls
* Multi-account support
* Post history database

---

# Example Prompts

LinkedIn:

```txt
Write a concise but thoughtful post about emerging AI systems and their effect on human creativity.
```

Twitter/X:

```txt
Write a short observational one-liner about technology and human behavior.
```

---

# Why This Exists

Partly because automation is fun.

Partly because I wanted to see whether AI-generated "thought leadership" could blend into real social platforms.

The results were interesting.

The posts looked polished, but over time they started converging toward the same vague patterns and abstractions.

Ironically, the automation system itself became more interesting than the content it produced.

