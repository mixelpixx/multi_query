import gradio as gr
import openai
import google.generativeai as genai
import chromadb
import llama_index
from backend.rag_function import query_engine
from llms.openai_chat import openai_chat
from llms.gemini_chat import gemini_chat

# Define the chatbot function
def chatbot(input_text, llm):
    # Query the database with the user's input
    db_results = query_engine(input_text)
    
    # Depending on the selected LLM, use the appropriate function to generate a response
    if llm == 'OpenAI':
        response = openai_chat(input_text, db_results)
    elif llm == 'Gemini':
        response = gemini_chat(input_text, db_results)
    
    # Use the Google Generative AI API to generate a more detailed response
    detailed_response = genai.generate_detailed_response(input_text)
    
    # Use the ChromaDB API to get the color scheme for the response
    color_scheme = chromadb.get_color_scheme(response)
    
    # Use the Llama Index API to get the llama index for the response
    llama_index = llama_index.get_llama_index(response)
    
    # Combine the response, detailed response, color scheme, and llama index into a single output
    output = {
        "response": response,
        "detailed_response": detailed_response,
        "color_scheme": color_scheme,
        "llama_index": llama_index
    }
    
    return output

# Create a Gradio interface for the chatbot
iface = gr.Interface(fn=chatbot, inputs=["text", gr.inputs.Dropdown(choices=['OpenAI', 'Gemini'])], outputs="text")

# Launch the Gradio interface
iface.launch()
