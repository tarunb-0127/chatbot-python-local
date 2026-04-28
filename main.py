from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os
from colorama import Fore, Style, init

init(autoreset=True)

load_dotenv()

template = '''

Answer the question below.

Here is the conversation history : {context}

Question : {question}

Answer: 

'''

model = OllamaLLM(
    model="llama3",
    base_url=os.getenv("OLLAMA_BASE_URL")
)

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation():
    context = ""
    print(Fore.CYAN + Style.BRIGHT + "Welcome to AI Chatbot! Type 'exit' to quit.\n")
    while True:
        user_input = input(Fore.GREEN + "You : " + Style.RESET_ALL)
        if user_input.lower() == "exit":
            print(Fore.YELLOW + "Goodbye! 👋")
            break
        result = chain.invoke({"context": context, "question": user_input})
        print(Fore.MAGENTA + "Bot : " + Style.RESET_ALL + str(result))
        print(Fore.BLUE + "-" * 50 + Style.RESET_ALL) 
        context += f"\nUser : {user_input}\nAI : {result}"

if __name__ == "__main__":
    handle_conversation()
