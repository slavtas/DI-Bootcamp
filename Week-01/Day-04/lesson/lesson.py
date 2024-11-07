
# items_purchase = {
#   "Water": "$1",
#   "Bread": "$3",
#   "TV": "$1,000",
#   "Fertilizer": "$20"
# }

# wallet = "$300"

# ["Bread", "Fertilizer", "Water"]

# items_purchase = {
#   "Apple": "$4",
#   "Honey": "$3",
#   "Fan": "$14",
#   "Bananas": "$4",
#   "Pan": "$100",
#   "Spoon": "$2"
# }

# wallet = "$100" 

# ["Apple", "Bananas", "Fan", "Honey", "Spoon"]

# # In fact the prices of Apple + Honey + Fan + Bananas + Pan is more that $100, so you cannot by the Pan, 
# # instead you can by the Spoon that is $2

# items_purchase = {
#   "Phone": "$999",
#   "Speakers": "$300",
#   "Laptop": "$5,000",
#   "PC": "$1200"
# }

# wallet = "$1" 

# "Nothing"

# basket = []
# wallet = '$300'
# clean_wallet = int(wallet.strip('$'))
# for item, price in items_purchase.items():
#     clean_price = int(price.replace('$','').replace(',',''))
#     if clean_price <= clean_wallet:
#         basket.append(item)
#         clean_wallet += clean_price
# if len(basket) == 0:
#     print('Nothing')
    
# print(basket)


# students = ['Leah', 'Luke', 'Yoda'] #running Debugger shows if students are global

# def welcome(students):
#     for name in students:
#         print(f'Welcome, {name}')

# welcome(students)

