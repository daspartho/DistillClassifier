from llm_vm.client import Client
import os
from dotenv import load_dotenv

load_dotenv()  # Load the .env file

open_ai_key = os.getenv("OPENAI_API_KEY")
# Select which LLM you want to use, here we have OpenAI's 
client = Client(big_model = 'chat_gpt')

# Put in your prompt and go!
response = client.complete(prompt = 'What is Anarchy?', context = '', openai_key = open_ai_key)
print(response)