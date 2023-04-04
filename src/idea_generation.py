import openai
import requests

def generate_idea(prompt, config):
    openai.api_key = config.get('API_KEYS', 'OPENAI_API_KEY')

    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )

    idea = response.choices[0].text.strip()
    return idea