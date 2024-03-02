import os
import shutil
from openai import OpenAI

def openai_chat(user_message, db_results):
    client = OpenAI()

    try:
        return client.chat.completions.create(
            model="gpt-3.5-turbo-16k",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message},
                {"role": "db_results", "content": db_results}
            ],
            stream=True
        )
    except Exception as e:
        print(f"Failed to call OpenAI API: {e}")
