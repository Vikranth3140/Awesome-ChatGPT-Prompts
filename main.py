from datasets import load_dataset
import random

dataset = load_dataset('fka/awesome-chatgpt-prompts')

def generate_prompt(dataset):
    prompts = dataset['prompt']
    return random.choice(prompts)

prompt = generate_prompt(dataset['train'])
print(prompt)