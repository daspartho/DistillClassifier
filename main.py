from generation import generate_dataset

generate_dataset(
    model="chat_gpt",
    columns={
        "text": "either spoiler or not spoiler text",
        "label": "if text is spoiler or not",
    },
    n_examples=25,
)
