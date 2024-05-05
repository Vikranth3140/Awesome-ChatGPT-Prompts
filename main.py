from datasets import load_dataset

def load_chatgpt_data():
    dataset = load_dataset('fka/awesome-chatgpt-prompts')['train']
    return dataset['act'], dataset['prompt']

def view_all(items, item_type):
    print(f"All {item_type}:")
    for idx, item in enumerate(items, start=1):
        print(f"{idx}: {item}")

def main():
    names, prompts = load_chatgpt_data()

    while True:
        print("\nOptions:")
        print("1. View All Names")
        print("2. View All Prompts")
        print("3. Input prompt number")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            view_all(names, "Names")
        elif choice == '2':
            view_all(prompts, "Prompts")
        elif choice == '3':
            prompt_number = int(input("Enter the prompt number: "))
            if 1 <= prompt_number <= len(prompts):
                print("Selected prompt:")
                print(prompts[prompt_number - 1])
            else:
                print("Invalid prompt number. Please try again.")
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()