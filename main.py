from llm_vm.client import Client
import os
from dotenv import load_dotenv

load_dotenv()  # Load the .env file

open_ai_key = os.getenv("OPENAI_API_KEY")
# Select which LLM you want to use, here we have OpenAI's 
client = Client(big_model = 'pythia')

generation_prompt = """Generate 40 examples of conversations, where an initial statement is made, followed by two replies, one that agrees with the initial statement and one that disagrees with the initial statement. The initial statement could be right, wrong, or neither right nor wrong.

Structure of the conversation like this:
[
  {
    "statement": "<initial statement>",
    "agree": "<reply that agrees with the initial statement>",
    "disagree": "<reply that disagrees with the initial statement>"
  },
  {
    "statement": "<initial statement>",
    "agree": "<reply that agrees with the initial statement>",
    "disagree": "<reply that disagrees with the initial statement>"
  }
]"""

# Put in your prompt and go!
response = client.complete(prompt = generation_prompt, context = '', openai_key = open_ai_key)
print(response)