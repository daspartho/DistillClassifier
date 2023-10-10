from llm_vm.client import Client
import os
from dotenv import load_dotenv
import json

load_dotenv()  # Load the .env file

open_ai_key = os.getenv("OPENAI_API_KEY")


def generate_dataset(model, n_call, columns, filename="dataset.json"):
    columns_prompt = ""

    for key, value in columns.items():
        columns_prompt += f"- {key}: {value}\n"

    generation_prompt = f"""I'm trying to create a dataset. 

Here are the columns for the dataset:
{columns_prompt}

Generate entries for the dataset as an array of JSON Object. Do not include any explanations, only provide a RFC8259 compliant JSON response strictly following the above information on the columns for the dataset without deviation."""

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
    generate_dataset(
        model="chat_gpt",
        columns={
            "text": "either spoiler or not spoiler text",
            "label": "if text is spoiler or not",
        },
        n_call=3,
    )
