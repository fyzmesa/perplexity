import requests
import json
import openai

openai.api_key = "[OPENAIAPIKEY]"

user_input = input('Please ask your question:\n> ')

models = ['llama-2-70b-chat',
          'llama-2-13b-chat',
          'codellama-34b-instruct',
          'mistral-7b-instruct']

url = "https://api.perplexity.ai/chat/completions"

headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Bearer [pplx-APIKEY]"
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

print(f"Model: gpt-3.5-turbo-0613")
print(chatcompletion(user_input))
