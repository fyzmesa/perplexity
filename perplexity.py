import requests
import json

# Set your API key as an environment variable
api_key = "PPLXAPIKEY"

# Define the endpoint URL for translation
url = "https://api.perplexity.ai/chat/completions"

# Set the headers with the API key
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

source = "我叫科林，是一名初级 Python 开发人员，正在尝试使用 perplexity api。"

# Define the payload with the Chinese sentence
payload = {
    "model": "llama-3.1-8b-instruct",  # Specify the model if required by the API
    "messages": [
        {"role": "user",
             "content": "Please translate this Chinese text in English:" + source}
    ]
}

# Make the POST request
response = requests.post(url, headers=headers, json=payload)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    output = response.json()
    # Extract and print the translated text
    translated_text = output.get('choices')[0].get('message').get('content')
    print("Translated Text:", translated_text)
else:
    # Print the error details
    print("Error:", response.status_code, response.text)
