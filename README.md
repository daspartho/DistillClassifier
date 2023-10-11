# DistillClassifier

## About
DistillClassifier is a tool built on top of [LLM-VM](https://github.com/anarchy-ai/LLM-VM) to easily generate synthetic data for classification tasks using LLMs for distilling LLM knowledge for classification task into much smaller and faster-to-run classification models. 

This project was build for the ANARCHY October 2023 Hackathon. Checkout ANARCHY on their [github](https://github.com/anarchy-ai) and [website](https://anarchy.ai/welcome/why_anarchy).

## Team Members:

- [Partho Das](https://github.com/daspartho)
- [Karan Janthe](https://github.com/kmj-007)

## Setup

### clone the project from github

```bash
git clone https://github.com/daspartho/DistillClassifier
```

### `cd` into the project

```bash
cd DistillClassifier
```

### install LLM-VM

```bash
git clone https://github.com/anarchy-ai/LLM-VM.git
cd LLM-VM
pip3 install .
cd ..
```

### install python dependencies

```bash
pip3 install -r requirements.txt
```

### create an `.env` with the following (if you want to use openai models):

```bash
OPENAI_API_KEY=
```

## Run

### You can run the tool from command line like this:

```bash
python3 generation.py <columns> <n_examples> [-m <model>] [-f <filename>]
```

### Arguments:

- `<columns>`: Column information as a dictionary.
- `<n_examples>`: Number of examples to be generated.
- `-m, --model`: (Optional) Model name. Defaults to "chat_gpt".
- `-f, --filename`: (Optional) Dataset filename. Defaults to "dataset.json".

### Example:

```bash
python3 generation.py '{"text": "either spoiler or not spoiler text", "label": "if text is spoiler or not"}' 25 -m 'chat_gpt' -f 'dataset.json'
```

### or run the `demo.py` file directly:

```bash
python3 demo.py
```

### example output dataset:

#### [demo_dataset.json](/demo_dataset.json)


### LICENSE
MIT