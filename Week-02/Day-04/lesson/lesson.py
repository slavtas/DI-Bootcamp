# # RegEx
# # re.findall() ++++++++++++++++++
# import re
# string = "at what time?"
# match = re.findall('at',string)
# print (match)

# # re.search() ++++++++++++++++++++
# import re

# string = "at what time?"
# match = re.search('at',string)
# if (match):
#     print ("String found at: ") ,match.start()
# else:
#     print ("String not found!")

# string = "at what time?"
# match = re.search('of',string)
# if (match):
#     print ("String found at: ") ,match.start()
# else:
#     print ("String not found!")

# # re.split() ++++++++++++++++++++++
# import re

# string = "at what time?"
# match = re.split('a',string)
# print (match)

# # re.sub()+++++++++++++++++++++++++++++
# import re

# string = "at what time?"
# match = re.sub("\s","!!!",string)
# print (match)

# import random

# list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]

# target_number = 3728

# def find_pairs_with_sum(numbers, target):

#     seen = set()
#     pairs = set()

#     for number in numbers:
#         complement = target - number
#         if complement in seen:
           
#             pairs.add(tuple(sorted((number, complement))))
#         seen.add(number)

#     return list(pairs)

# pairs = find_pairs_with_sum(list_of_numbers, target_number)

# for pair in pairs:
#     print(f"{pair[0]} and {pair[1]} sum to the target_number {target_number}")

# print(f"\nTotal unique pairs found: {len(pairs)}")

# squares = [x*x for x in range(1, 6)]
# print(squares)

import requests
response = requests.get('https://api.chucknorris.io/')
print(response.status_code)
print(response.text)
# print(response.json())
print(response.headers)
