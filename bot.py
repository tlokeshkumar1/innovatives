import openai_secret_manager

assert "openai" in openai_secret_manager.get_services()
secrets = openai_secret_manager.get_secret("openai")

import openai

openai.api_key = secrets["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"]

def generate_response(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.7,
        max_tokens=150,
        n=1,
        stop=None,
    )

    message = response.choices[0].text.strip()
    return message

while True:
    user_input = input("You: ")

    prompt = f"User: {user_input}\nChatGPT: "
    response = generate_response(prompt)

    print("ChatGPT:", response)
