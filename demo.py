from generation import generate_dataset

generate_dataset(
    columns={
        "text": "either spoiler or not spoiler text",
        "label": "if text is spoiler or not",
    },
    n_examples=25,
    model="chat_gpt",
    filename="demo_dataset.json",
)
