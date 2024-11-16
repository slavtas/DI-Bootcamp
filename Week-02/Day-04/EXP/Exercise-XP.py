# Exercise_1 Random Sentence Generator
import random

def get_words(filename):
        with open(r'C:\Users\User\Desktop\DI-Bootcamp\Week-02\Day-04\EXP\word_list.txt', 'r') as file:
            words = file.read().splitlines()
        return words

def get_random_sentence(length, words):
    random_words = random.sample(words, length)
    return ' '.join(random_words).lower()

def main():
    print("Welcome to the Random Sentence Generator!")
    print("This program generates a random sentence using words from a file.")

    user_input = input("Enter the length of the sentence (between 2 and 20 words): ")
    
    if not user_input.isdigit() or not (2 <= int(user_input) <= 20):
        print("Error: Please enter a valid number between 2 and 20.")
        return

    length = int(user_input)

    words = get_words('word_list.txt')

    sentence = get_random_sentence(length, words)
    print(f"Generated sentence: {sentence}")

if __name__ == "__main__":
    main()
# +++++++++++++++++++++++++++++++++++++++++++++++++++ #

# Exercise_2 Working With JSON
import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

def parse_json(json_string):
    """Parse the JSON string into a Python dictionary."""
    return json.loads(json_string)

def access_nested_key(data, keys):
    """Access a nested key in a dictionary using a list of keys."""
    for key in keys:
        data = data[key]
    return data

def add_key(data, keys, new_key, new_value):
    """Add a new key at the desired level in the dictionary."""
    target = data
    for key in keys:
        target = target[key]
    target[new_key] = new_value

def save_json_to_file(data, filename):
    """Save the modified dictionary to a JSON file."""
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

# Main logic
# Step 1: Parse JSON
data = parse_json(sampleJson)

# Step 2: Access the "salary" key
salary = access_nested_key(data, ["company", "employee", "payable", "salary"])
print(f"Salary: {salary}")

# Step 3: Add a new key "birth_date"
add_key(data, ["company", "employee"], "birth_date", "1985-10-26")

# Step 4: Save to file
save_json_to_file(data, "modified_sample.json")
print("Updated JSON saved to 'modified_sample.json'.")