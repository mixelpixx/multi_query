"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_NONE"
  },
]

def gemini_chat(user_message):
    model = genai.GenerativeModel(model_name="gemini-1.0-pro-001",
                                generation_config=generation_config,
                                safety_settings=safety_settings)

    return model.start_chat(history=[
        {
            "role": "user",
            "parts": [user_message]
        },
        {
            "role": "model",
            "parts": ["I am well, thank you for asking. I am a virtual assistant designed to help you with a variety of tasks, including answering your questions, providing information, and completing tasks. How can I help you today?"]
        },
    ])

convo = gemini_chat("Hi, how are you today?")
convo.send_message("YOUR_USER_INPUT")
print(convo.last.text)
