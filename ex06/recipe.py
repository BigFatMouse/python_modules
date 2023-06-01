cookbook = {
    'sandwich': {
        'ingredients':  ['ham', 'bread', 'cheese', 'tomatoes'],
        'meal': 'lunch',
        'prep_time': 10
        },
    'cake': {
        'ingredients':  ['flour', 'sugar', 'eggs'],
        'meal': 'dessert',
        'prep_time': 60
        },
    'salad': {
        'ingredients':  ['avocado', 'arugula', 'tomatoes', 'spinach'],
        'meal': 'lunch',
        'prep_time': 15
        }
    }

def print_names():
    print('List of recipes in the cookbook:')
    print('    '+', '.join(cookbook.keys()) + '\n')


def print_recipe():
    name = input('Please enter a recipe name to get its details:\n').lower()
    if name in cookbook.keys():
        print(f"Recipe for {name}:")
        print("    Ingredients list:", cookbook[name]['ingredients'])
        print(f"    To be eaten for {cookbook[name]['meal']}.")
        print(f"    Takes {cookbook[name]['prep_time']} minutes of cooking.\n")
    else:
        print('No such recipe\n')


def del_recipe():
    name = input('Please enter a recipe name to delete:\n').lower()
    if name in cookbook.keys():
        cookbook.pop(name)
        print(f"{name} is deleted\n")
    else:
        print('No such recipe\n')


def add_recipe():
    name = input('Enter a name:\n').lower()
    print('Enter ingredients: ')
    ingredients = []
    while True:
        line = input()
        if line:
            ingredients.append(line)
        else:
            break
    cookbook[name] = {}
    cookbook[name]['ingredients'] = ingredients
    cookbook[name]['meal'] = input('Enter a meal type:\n')
    cookbook[name]['prep_time'] = input('Enter a preparation time:\n')


if __name__ == '__main__':
    funcs = {
        '1': add_recipe,
        '2': del_recipe,
        '3': print_recipe,
        '4': print_names
    }
    options = '''List of available option:
    1: Add a recipe
    2: Delete a recipe
    3: Print a recipe
    4: Print the cookbook
    5: Quit'''

    print('Welcome to the Python Cookbook !')
    print(options)

    while True:
        opt = input('Please select an option:\n')
        if not opt.isdigit() or int(opt) < 0 or int(opt) > 5:
            print('Sorry, this option does not exist.')
            print(options)
        elif opt == '5':
            print('Cookbook closed. Goodbye !\n')
            break
        else:
            funcs[opt]()


        # if opt == '1':
        #     add_recipe()
        # elif opt == '2':
        #     del_recipe()
        # elif opt == '3':
        #     print_recipe()
        # elif opt == '4':
        #     print_names()
        # elif opt == '5':
        #     print('Cookbook closed. Goodbye !\n')
        #     break
        # else:
        #     print('Sorry, this option does not exist.')
        #     print(options)
