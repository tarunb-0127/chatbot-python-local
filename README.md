
Python Ollama Chatbot
=====================

<img width="1158" height="415" alt="image" src="https://github.com/user-attachments/assets/b3b2cab8-09d9-459e-b895-11990d86923a" />




This project is a simple interactive chatbot built with LangChain and Ollama. It connects to an Ollama server (running locally or in Docker) and uses the `llama3` model to answer user questions.

Features
--------
- Interactive command-line chatbot.
- Maintains conversation history for context-aware responses.
- Uses `.env` file to store configuration (Ollama server URL).
- Built with LangChain's `ChatPromptTemplate` and `OllamaLLM`.

Requirements
------------
- Python 3.9+
- Ollama running locally or in Docker.
- Dependencies:
  pip install langchain langchain-ollama langchain-core python-dotenv

Setup
-----
1. Clone the repository.
2. Create a `.env` file in the project root:
   OLLAMA_BASE_URL=http://localhost:11434
3. Run Ollama in Docker:
   docker run -d --name myllama -p 11434:11434 ollama/ollama
   docker exec -it myllama ollama pull llama3
4. Start the chatbot:
   python chatbot.py

Usage
-----
- Type your questions in the terminal.
- The chatbot will respond using the LLaMA model.
- Type `exit` to quit.

Example
-------
Welcome to AI Chatbot! Type 'exit' to quit.
You : Hello
Bot : Hi there! How can I help you today?

Notes
-----
- The conversation history is stored in memory during runtime.
- Update `.env` if your Ollama server runs on a different host or port.

---
