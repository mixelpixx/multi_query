import os
import shutil
from openai import OpenAI

def openai_chat(user_message):
    client = OpenAI()

    return client.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message}
        ],
        stream=True
    )
