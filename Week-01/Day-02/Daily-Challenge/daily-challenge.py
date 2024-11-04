# Challenge_1 Numbers and length
number = int(input('Enter a number: '))
length = int(input('Enter the length of the list: '))

multiples_list = []

for i in range(1, length + 1):
    multiples_list.append(number * i)

print(multiples_list)

# Challenge_2 Removing duplicate consecutive letters
def remove_consecutive_duplicates(s):
    result = ''
    previous_char = ''
    
    for char in s:
        if char != previous_char:
            result += char
        previous_char = char

    return result

user_word = input('Type your word: ')

new_string = remove_consecutive_duplicates(user_word)
print(f'Refined result without consecutive duplicates: {new_string}')