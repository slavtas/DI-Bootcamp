# Challenge_1 Ask for a word, create dict, store indexes for each letter in a list
words_letter_indexes = {}

while True:
    word = input('Type a word, enter "done" when finished: ')
    if word == "done":
        break
    letter_indexes = {}
    for index, letter in enumerate(word):
        if letter in letter_indexes:
            letter_indexes[letter].append(index)
        else:
            letter_indexes[letter] = [index]
    words_letter_indexes[word] = letter_indexes

print('Here is what you get: ', words_letter_indexes)
print("Now, let's make it look nice:")
for word, indexes in words_letter_indexes.items():
    print(f'{word} {indexes}')

#Challenge_2 Gone shopping

def convert_to_number(amount):
    return float(amount.replace('$', '').replace(',', ''))

def get_affordable_items(items_purchase, wallet):
    wallet_amount = convert_to_number(wallet)
    affordable_items = []

    for item, price in items_purchase.items():
        item_price = convert_to_number(price)
        if wallet_amount >= item_price:
            affordable_items.append(item)

    affordable_items.sort()

    return affordable_items if affordable_items else "Nothing"

items_purchase_1 = {
    "Water": "$1",
    "Bread": "$3",
    "TV": "$1,000",
    "Fertilizer": "$20"
}
wallet_1 = "$300"
print(get_affordable_items(items_purchase_1, wallet_1))

items_purchase_2 = {
    "Apple": "$4",
    "Honey": "$3",
    "Fan": "$14",
    "Bananas": "$4",
    "Pan": "$100",
    "Spoon": "$2"
}
wallet_2 = "$100"
print(get_affordable_items(items_purchase_2, wallet_2))

items_purchase_3 = {
    "Phone": "$999",
    "Speakers": "$300",
    "Laptop": "$5,000",
    "PC": "$1200"
}
wallet_3 = "$1"
print(get_affordable_items(items_purchase_3, wallet_3))