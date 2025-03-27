import os
import requests

PROMPT = f"{os.environ.get('PROMPT')}"
API_KEY = f"{os.environ.get('GOOGLE_API_KEY')}"
CLIENT_ID = f"{os.environ.get('LINKEDIN_CLIENT_ID')}"
CLIENT_SECRET = f"{os.environ.get('LINKEDIN_CLIENT_SECRET')}"
ACCESS_TOKEN = f"{os.environ.get('LINKEDIN_ACCESS_TOKEN')}"
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

def get_ai_data(prompt):
	payload = {
	"contents": [
		{
		"parts": [
			{
			"text": prompt
			}
		]
		}
	]
	}
	
	headers = {
	"Content-Type": "application/json"
	}

	
	response = requests.post(url, json=payload, headers=headers)

	
	if response.status_code == 200:
		
		data = response.json()
		
		return data["candidates"][0]["content"]["parts"][0]["text"]
	else:
		print(f"Error {response.status_code}")

def get_linkedin_userinfo(access_token):
    url = "https://api.linkedin.com/v2/userinfo"
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        user_data = response.json()
        return user_data
    else:
        print(f"Error fetching user info: {response.status_code}")
        return None

def get_linkedin_urn(access_token):
    url = "https://api.linkedin.com/v2/me"
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        profile_data = response.json()
        return profile_data.get('id')  
    else:
        print(f"Error fetching LinkedIn URN: {response.status_code}")
        return None


def post_to_linkedin(access_token, text_content):
    user_data = get_linkedin_userinfo(access_token)
    if not user_data or 'sub' not in user_data:
        print("Failed to retrieve user data.")
        return
    
    member_id = user_data['sub']    
    url = "https://api.linkedin.com/v2/ugcPosts"
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json',
        'X-Restli-Protocol-Version': '2.0.0'
    }
    
    payload = {
        "author": f"urn:li:person:{member_id}",  
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": text_content
                },
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }
    
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 201:
        print("Successfully posted to LinkedIn!")
        return response.json()
    else:
        print(f"Error posting to LinkedIn: {response.status_code}")
        print(response.text)
        return None

import random

def should_post():
    # 2 posts out of 12 attempts (twice a day)
    return random.randint(1, 12) <= 2

def main():
    if should_post():
        print("Proceeding to post on LinkedIn...")
	    text_content = get_ai_data(PROMPT)
	    result = post_to_linkedin(ACCESS_TOKEN, text_content)
	    if result:
	        print("Post successful!")
	    else:
	        print("Failed to post.")
    else:
        print("Skipping this run. Will try again later.")
	    
if __name__ == "__main__":
    main()
