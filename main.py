from datasets import load_dataset

def load_chatgpt_names():
    return load_dataset('fka/awesome-chatgpt-prompts')['train']['act']

def load_chatgpt_prompts():
    return load_dataset('fka/awesome-chatgpt-prompts')['train']['prompt']

def view_all_names(names):
    print("All Names:")
    for idx, name in enumerate(names, start=1):
        print(f"{idx}: {name}")

def view_all_prompts(prompts):
    print("All Prompts:")
    for idx, prompt in enumerate(prompts, start=1):
        print(f"{idx}: {prompt}")

def get_user_input():
    print("\nOptions:")
    print("1. View All Names")
    print("2. View All Prompts")
    print("3. Input prompt number")
    print("4. Exit")
    choice = input("Enter your choice: ")
    return choice

def main():
    names = load_chatgpt_names()
    prompts = load_chatgpt_prompts()

    while True:
        choice = get_user_input()

        if choice == '1':
            view_all_names(names)
        elif choice == '2':
            view_all_prompts(prompts)
        elif choice == '3':
            prompt_number = int(input("Enter the prompt number: "))
            if prompt_number < 1 or prompt_number > len(prompts):
                print("Invalid prompt number. Please try again.")
            else:
                print("Selected prompt:")
                print(prompts[prompt_number - 1])
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()