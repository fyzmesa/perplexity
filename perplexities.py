import requests
import json
import openai
from bs4 import BeautifulSoup

openai.api_key = ""
gurl = 'https://www.google.com/search'

user_input = input('Please ask your question:\n> ')
# How many stars are present in the universe?

models = ['llama-2-70b-chat',
          'llama-2-13b-chat',
          'codellama-34b-instruct',
          'mistral-7b-instruct']
          # 'replit-code-v1_5-3b']

url = "https://api.perplexity.ai/chat/completions"

headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": ""
}

for model in models:
    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": "Be precise and concise."
            },
            {
                "role": "user",
                "content": user_input
            }
        ]
    }

    response = requests.post(url, json=payload, headers=headers)

    output = json.loads(response.text)

    print(f"Model: {model}")
    for item in output['choices']:
        perplexity_output = item['message']['content']
        print(perplexity_output)
    print("\n")


def chatcompletion(user_input):
    output = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        temperature=1,
        presence_penalty=0,
        frequency_penalty=0,
        messages=[
            {"role": "system", "content": "Be precise and concise."},
            {"role": "user", "content": user_input}
        ],
    )

    for item in output['choices']:
        chatgpt_output = item['message']['content']

    return chatgpt_output

gheaders = {
	'Accept' : '*/*',
	'Accept-Language': 'en-US,en;q=0.5',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82',
}
gparameters = {'q': user_input}

content = requests.get(gurl, headers = gheaders, params = gparameters).text
soup = BeautifulSoup(content, 'html.parser')

search = soup.find(id = 'search')
first_link = search.find('a')

print(f"Model: gpt-3.5-turbo-0613")
print(chatcompletion(user_input))

print("Google search")
print(first_link['href'])
