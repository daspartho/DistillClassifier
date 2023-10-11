from llm_vm.client import Client
import os
from dotenv import load_dotenv
import json
import argparse
from datasets import load_dataset

load_dotenv()  # Load the .env file

open_ai_key = os.getenv("OPENAI_API_KEY")
hf_token = os.getenv("HF_HUB_TOKEN")


def generate_dataset(columns, n_examples, model, filename):
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

    while len(dataset) < n_examples:
        response = client.complete(
            prompt=generation_prompt, openai_key=open_ai_key, temperature=0.7
        )
        try:
            data = json.loads(response["completion"])
        except:
            print("response skipped")
            continue
        dataset.extend(data)
        print(f"{len(dataset)}/{n_examples} examples generated")

    dataset = dataset[:n_examples]

    print(f"writing dataset to {filename}...")
    with open(filename, "w") as f:
        json.dump(dataset, f, indent=2)
    print("done!")


def upload_dataset(filename, repo_id):
    print(f"uploading {filename} to {repo_id}...")
    dataset = load_dataset("json", data_files=filename)
    dataset.push_to_hub(repo_id, token=hf_token)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("columns", help="column information as a dictionary")
    parser.add_argument("n_examples", type=int, help="number of examples to be generated")
    parser.add_argument("-m", "--model", default="chat_gpt", help="model name")
    parser.add_argument("-f", "--filename", default="dataset.json", help="dataset filename")
    parser.add_argument("-r", "--repo", help="huggingface repo id")
    args = parser.parse_args()

    generate_dataset(
        columns=eval(args.columns),
        n_examples=args.n_examples,
        model=args.model,
        filename=args.filename,
    )
    if args.repo:
        upload_dataset(args.filename, args.repo)


if __name__ == "__main__":
    main()
