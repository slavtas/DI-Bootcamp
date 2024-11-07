# Matrix
matrix = [
    [7,'i','i'],
    ['T','s','x'],
    ['h','%','?'],
    ['i',' ','#'],
    ['s','M',' '],
    ['$','a',' '],
    ['#','t','%'],
    ['^','r','!']
    ]
print(matrix)

decrypted_message = ''

rows = len(matrix)
cols = len(matrix[0])

for col in range(cols):

    for row in range(rows):
        element = matrix[row][col]
        
        if isinstance(element, str) and element.isalpha():
            decrypted_message += element
        elif decrypted_message and decrypted_message[-1] != " ":
            decrypted_message += " "

print("Decrypted Message:", decrypted_message)
