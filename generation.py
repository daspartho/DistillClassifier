from llm_vm.client import Client
import os
from dotenv import load_dotenv
import json

load_dotenv()  # Load the .env file

open_ai_key = os.getenv("OPENAI_API_KEY")

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


def generate_dataset(model, n_call, filename="dataset.json"):
    print("getting model...")
    client = Client(big_model=model)

    print("generating dataset...")
    dataset = []

    for i in range(n_call):
        print(f"api call {i+1}/{n_call}")
        response = client.complete(prompt=generation_prompt, openai_key=open_ai_key)
        try:
            data = json.loads(response["completion"])
        except:
            print("response skipped")
            continue
        dataset.extend(data)

    print(f"writing dataset to {filename}...")
    with open(filename, "w") as f:
        json.dump(dataset, f, indent=2)


if __name__ == "__main__":
    generate_dataset(model="chat_gpt", n_call=3)
