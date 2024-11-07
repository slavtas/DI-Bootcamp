# Exercise_1 What Am I Learning?
def display_message():
    print("I'm learning Fullstack Development")

display_message()

# ----------------------------------------------------------------------

# Exercise_2 What's Your Favorite Book?
def favorite_book(title):
    print(f'One of my favorite books is {title}')

favorite_book('Alice in Wonderland')

# ----------------------------------------------------------------------

# Exercise_3 Georaphy
def describe_city(city,country= "Israel"):
    print(f'{city} is in {country}')

describe_city('Tel-Aviv')
describe_city('Moscow', 'Russia')

# ----------------------------------------------------------------------

# Exercise_4 Random
import random

def compare_numbers(user_number):
    
    random_number = random.randint(1,100)
    if user_entered == random_number:
        print('You won billion buck!')
    else:
        print(f'You lost a fortune! Your number is {user_entered}. Try again!')
user_entered = input('Enter a number between 1 and 100 ')

compare_numbers(user_entered)

# ----------------------------------------------------------------------

# Exercise_5 Personalized Shirts
def make_shirt(size="large",text="I Love Python"):
    print(f'The size of the shirt is {size} and the text is {text}')

make_shirt('small','I love NY')
make_shirt()
make_shirt('medium')

# ----------------------------------------------------------------------

# Example_6 Maaagic
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians():
    for magician in magician_names:
        print(magician)
show_magicians()

def make_great():
    for i in range(len(magician_names)):
        magician_names[i] = magician_names[i] + ' the Great'
        
make_great()

show_magicians()

# ----------------------------------------------------------------------

# Exercise_7 Temperature Advice
import random

# def get_random_temp():
#     return random.randint(-10,40)
# print(get_random_temp()) #testing random temperatures
# print(get_random_temp()) #testing random temperatures
# print(get_random_temp()) #testing random temperatures

# def main():
#    temperature = get_random_temp()
#    print(f'The temperature right now is {temperature} degrees Celsius')
# main() #functionality has been checked

# def main():
#     season = input('Type in the season to know the temperature ')
#     temperature = get_random_temp()
#     print(f'The temperature right now is {temperature} degrees Celsius')

#     if temperature < 0:
#         print('Get back under the blanket and cancel all activities!')
#     elif 0 <= temperature < 16:
#         print('Don\'t forget your hat and coat!')
#     elif 16 <= temperature <= 23:
#         print('Seems like a great time to take a walk in the park!')
#     elif 24 <= temperature < 32:
#         print('Time to get your swimming suit and rush to the pool!')
#     elif 32 <= temperature <= 40:
#         print('Stay close to the AC unit and drink more water!')
# main()
          
# def get_random_temp(season):
    
#     if season == 'winter':
#         return random.randint(-10,14)
#     elif season == 'spring':
#         return random.randint(15,21)
#     elif season == 'summer':
#         return random.randint(22,40)

# def main():
#     season = input('Type in the season to know the temperature ')
#     temperature = get_random_temp(season)
#     print(f'The temperature right now is {temperature} degrees Celsius')

#     if temperature < 0:
#         print('Get back under the blanket and cancel all activities!')
#     elif 0 <= temperature < 16:
#         print('Don\'t forget your hat and coat!')
#     elif 16 <= temperature <= 23:
#         print('Seems like a great time to take a walk in the park!')
#     elif 24 <= temperature < 32:
#         print('Time to get your swimming suit and rush to the pool!')
#     elif 32 <= temperature <= 40:
#         print('Stay close to the AC unit and drink more water!')
# main()

# ----------------------------------------------------------------------
# Exercise_8 Nerd Check
data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]

def quiz_user():
    correct_count = 0
    incorrect_count = 0
    wrong_answers = []

    for item in data:
        question = item["question"]
        correct_answer = item["answer"]
        
        user_answer = input(f"{question} ")

        if user_answer == correct_answer:
            correct_count += 1
        else:
            incorrect_count += 1
            wrong_answers.append({
                "question": question,
                "user_answer": user_answer,
                "correct_answer": correct_answer
            })

    return correct_count, incorrect_count, wrong_answers

def display_results(correct_count, incorrect_count, wrong_answers):
    print(f"\nYou got {correct_count} correct and {incorrect_count} incorrect answers.")

    if wrong_answers:
        print("\nQuestions you got wrong:")
        for item in wrong_answers:
            print(f"- Question: {item['question']}")
            print(f"  Your Answer: {item['user_answer']}")
            print(f"  Correct Answer: {item['correct_answer']}\n")

    if incorrect_count > 3:
        print("You had more than 3 incorrect answers. Would you like to play again? (yes/no)")
        replay = input()
        if replay == "yes":
            main()  # Restart the game

def main():
    correct_count, incorrect_count, wrong_answers = quiz_user()
    display_results(correct_count, incorrect_count, wrong_answers)

# Run the quiz
main()