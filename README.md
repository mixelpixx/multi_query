# Language Learning Model Selection (LLMS) Project

## Description
This project is a chatbot application that allows the user to choose between two language learning models (LLMs): OpenAI and Gemini. The chatbot uses a database of documents to provide responses to user queries. The database can be rebuilt if necessary.

## Installation
To set up the project, follow these steps:

1. Clone the repository to your local machine.
2. Install the necessary dependencies. This project requires the `openai`, `google-generativeai`, `gradio`, `chromadb`, and `llama_index` packages. You can install these with pip:
   ```
   pip install openai google-generativeai gradio chromadb llama_index
   ```
3. Set up your environment variables. You will need to provide your OpenAI API key and Gemini API key.

## Usage
To use the project, run the `chatbot_gui.py` script in the `/GUI` directory. This will launch a Gradio interface where you can input your message and choose your LLM.

## File Structure
- `/backend/rag_function.py`: Contains functions for checking if the database exists, rebuilding the database, and querying the engine.
- `/docs/placeholder doc.txt`: A placeholder for the project documentation.
- `/GUI/chatbot_gui.py`: Contains the main chatbot interface.
- `/llms/openai_chat.py`: Contains the function for chatting with the OpenAI model.
- `/llms/gemini_chat.py`: Contains the function for chatting with the Gemini model.

## Contributing
Contributions are welcome. Please submit a pull request.

## License
This project is licensed under the terms of the MIT license.