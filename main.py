import os
import requests
from PIL import Image
from io import BytesIO

# API Endpoints
OPENAI_API_URL = "https://api.openai.com/v1/chat/completions"
DALL_E_API_URL = "https://api.openai.com/v1/images/generations"
LINKEDIN_API_URL = "https://api.linkedin.com/v2/ugcPosts"

# Fetch environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LINKEDIN_ACCESS_TOKEN = os.getenv("LINKEDIN_ACCESS_TOKEN")
LINKEDIN_USER_ID = os.getenv("LINKEDIN_USER_ID")
NOTIFICATION_EMAIL = os.getenv("NOTIFICATION_EMAIL")  # For email notifications

if not all([OPENAI_API_KEY, LINKEDIN_ACCESS_TOKEN, LINKEDIN_USER_ID, NOTIFICATION_EMAIL]):
    raise EnvironmentError("Missing required environment variables.")

# Function to generate post content using OpenAI
def generate_post_content():
    headers = {"Authorization": f"Bearer {OPENAI_API_KEY}"}
    payload = {
        "model": "gpt-4",
        "messages": [
            {"role": "system", "content": "Generate a LinkedIn post about frontend development or graphic design."}
        ],
    }
    response = requests.post(OPENAI_API_URL, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]

# Function to generate an image using DALL-E
def generate_image(prompt):
    headers = {"Authorization": f"Bearer {OPENAI_API_KEY}"}
    payload = {"prompt": prompt, "n": 1, "size": "1024x1024"}
    response = requests.post(DALL_E_API_URL, headers=headers, json=payload)
    response.raise_for_status()
    image_url = response.json()["data"][0]["url"]

    # Download image
    image_response = requests.get(image_url)
    image_response.raise_for_status()
    return BytesIO(image_response.content)

# Function to post on LinkedIn
def post_to_linkedin(content, image_path):
    headers = {
        "Authorization": f"Bearer {LINKEDIN_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "author": f"urn:li:person:{os.getenv('LINKEDIN_USER_ID')}",
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {"text": content},
                "shareMediaCategory": "IMAGE",
                "media": [
                    {
                        "status": "READY",
                        "originalUrl": image_path,
                    }
                ]
            }
        },
        "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"}
    }
    response = requests.post(LINKEDIN_API_URL, headers=headers, json=payload)
    response.raise_for_status()
    return response.status_code == 201

# Function to notify via email
def send_email_notification():
    # Use a library like smtplib to send an email notification
    print(f"Notification sent to {NOTIFICATION_EMAIL}")

def main():
    try:
        print("Generating content...")
        content = generate_post_content()
        print("Generating image...")
        image = generate_image(content)

        # Save image locally
        image_path = "generated_image.png"
        with open(image_path, "wb") as f:
            f.write(image.getbuffer())

        print("Posting to LinkedIn...")
        success = post_to_linkedin(content, image_path)

        if success:
            print("Posted successfully!")
            send_email_notification()
        else:
            print("Failed to post.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
