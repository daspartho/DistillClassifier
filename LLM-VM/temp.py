from llm_vm.client import Client

# Select which LLM you want to use, here we have OpenAI's 
client = Client(big_model = 'chat_gpt')

# Put in your prompt and go!
response = client.complete(prompt = 'What is Anarchy?', context = '', openai_key = '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')
print(response)