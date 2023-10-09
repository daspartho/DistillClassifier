 # import our client
from llm_vm.client import Client
import os
import load_dotenv

load_dotenv()  # Load the .env file

# Select which LLM you want to use, here we have OpenAI's 
client = Client(big_model = 'chat_gpt')

# Load your API key from an environment variable
openai_api_key = os.getenv("OPENAI_API_KEY")
# Put in your prompt and go!
response = client.complete(prompt = 'how is the weather in delhi?', context = '', openai_key = openai_api_key)
print(response)
# Anarchy is a political ideology that advocates for the absence of government...
