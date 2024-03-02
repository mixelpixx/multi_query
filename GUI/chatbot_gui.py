import gradio as gr
from backend.rag_function import check_database_exists, rebuild_database
from llms.openai_chat import openai_chat
from llms.gemini_chat import gemini_chat

def chatbot_interface(user_message, llm_choice):
    if llm_choice == 'OpenAI':
        return openai_chat(user_message)
    elif llm_choice == 'Gemini':
        return gemini_chat(user_message)

if check_database_exists():
    rebuild_choice = gr.Interface.load()
    if rebuild_choice == 'Rebuild':
        rebuild_database()

llm_choice = gr.Radio(['OpenAI', 'Gemini'], label='Choose your LLM')
iface = gr.Interface(chatbot_interface, ['textbox', llm_choice], 'textbox')
iface.launch()