from datasets import load_dataset

def load_chatgpt_names():
    return load_dataset('fka/awesome-chatgpt-prompts')['train']['act']

def load_chatgpt_prompts():
    return load_dataset('fka/awesome-chatgpt-prompts')['train']['prompt']

def get_user_input(prompts, names):
    print("Choose a prompt number from 0 to", len(prompts) - 1)
    for idx, prompt in enumerate(names):
        print(f"{idx}: {names}")
    prompt_number = int(input("Enter the prompt number: "))
    if prompt_number < 0 or prompt_number >= len(prompts):
        print("Invalid prompt number. Please try again.")
        return get_user_input(prompts)
    return prompts[prompt_number]

def main():
    prompts = load_chatgpt_prompts()
    names = load_chatgpt_names()
    user_prompt = get_user_input(prompts, names)
    print("Selected prompt:")
    print(user_prompt)

if __name__ == "__main__":
    main()