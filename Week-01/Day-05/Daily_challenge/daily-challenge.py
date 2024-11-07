# Challenge_1 Sorting alphabetically
# def sorted_words():
#     words = input("Type in several worlds separated by commas: ").split(",")
#     sorted_words = [word for word in sorted(words)]
#     print(",".join(sorted_words))
# sorted_words()
# ----------------------------------

# Challenge_2 Longest Word
def longest_word(sentence):
    words = sentence.split()
    longest = max(words, key=len)
    return longest
sentences = []

while True:
    sentence = input("Enter sentence or type 'done' to finish: ")
    if sentence == 'done':
        break
    sentences.append(sentence)
    print("The longest word is:", longest_word(sentence))

print("\nSentences")

for i, sentence in enumerate(sentences, start=1):
    print(f'{i}. {sentence}')

