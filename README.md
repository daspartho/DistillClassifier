# DistillClassifier
Library to easily generate synthetic data for classification tasks using LLMs and train classification models on the generated data.

This project was build for the ANARCHY October 2023 Hackathon. Checkout ANARCHY on their [website](https://github.com/anarchy-ai) and [github](https://anarchy.ai/welcome/why_anarchy).

## Team Members:

- [Partho Das](https://github.com/daspartho)
- [Karan Janthe](https://github.com/kmj-007)

## setup

### Clone and Deploy

```bash
git clone https://github.com/daspartho/DistillClassifier
```

Install the dependency:

```bash
poetry install
```

create .env with following(if you want to use open-ai model):

```bash
OPENAI_API_KEY=
```

## run

you can run this from command line or streamlit app

command line:

```bash
python generation.py <columns> <n_examples> [-m <model>] [-f <filename>]
```

### Arguments:

- `<columns>`: Column information as a dictionary.
- `<n_examples>`: Number of examples to be generated.
- `-m, --model`: (Optional) Model name. Defaults to "chat_gpt".
- `-f, --filename`: (Optional) Dataset filename. Defaults to "dataset.json".


**Example:**

```bash
python generation.py 
    -c '{
        "text": "either spoiler or not spoiler text",
        "label": "if text is spoiler or not"
    }' 
    25 
    -m chat_gpt 
    -f demo_dataset.json
```

or run the demo file directly:

```bash
python demo.py
```

example output of dataset:

### [demo_dataset.json](/demo_dataset.json)


### LICENSE
MIT