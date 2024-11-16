from anagram_checker import AnagramChecker

def clean_input(user_input):
    """
    Clean and validate the user's input by removing leading/trailing spaces and converting to lowercase.
    Ensure the input is a single word with no special characters or spaces.
    """
    cleaned_input = user_input.strip()
    if not cleaned_input.isalpha():
        return None
    return cleaned_input.lower()

def show_menu():
    """
    Display the menu options for the user.
    """
    print("\nAnagram Checker Menu:")
    print("1. Input a word to check for anagrams")
    print("2. Exit the program")

def main():
    """
    Main function to run the Anagram Checker program.
    """
    checker = AnagramChecker('anagrams.txt')
    results = {"valid": 0, "invalid": 0}

    while True:
        show_menu()
        choice = input("Please select an option (1/2): ").strip()

        if choice == '1':
            user_word = input("Enter a word: ").strip()

            # Validate the word
            valid_word = clean_input(user_word)
            if not valid_word:
                print("Error: Please enter a valid single word with alphabetic characters only.")
                results["invalid"] += 1
                continue

            # Check if the word is valid
            if checker.is_valid_word(valid_word):
                print(f"YOUR WORD: \"{valid_word.upper()}\" is a valid English word.")
                anagrams = checker.get_anagrams(valid_word)
                if anagrams:
                    print(f"Anagrams for your word: {', '.join(sorted(anagrams))}")
                else:
                    print("No anagrams found.")
                results["valid"] += 1
            else:
                print(f"\"{valid_word.upper()}\" is not a valid English word.")
                results["invalid"] += 1

        elif choice == '2':
            print(f"\nGame Summary:")
            print(f"Valid words: {results['valid']}")
            print(f"Invalid words: {results['invalid']}")
            print("Thank you for using Anagram Checker!")
            break
        else:
            print("Invalid choice, please select 1 or 2.")

if __name__ == "__main__":
    main()