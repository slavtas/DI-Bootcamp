# * simple sequence **more complex e.g. dict

# def my_pets(*args):
#     print(args)
#     total_pets = len(args)
#     return total_pets

# print(my_pets('cat','dog','fish'))

def user_info(**kwargs):
    for keyword in kwargs.keys():
        if keyword == 'Slums':
            print(f'You stink, {name}')
    
    print(kwargs)

user_info(name = 'Bob', address = 'Slums', email = 'bob@slums.com')