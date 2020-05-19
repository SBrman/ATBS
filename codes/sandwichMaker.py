#! python3

import pyinputplus as pyip

ingredients = {'bread':   ['wheat', 'white', 'sourdough'],\
               'protein': ['chicken', 'turkey', 'ham', 'tofu'],\
               'cheese':  ['cheddar', 'Swiss', 'mozzarella'],\
               'sides':  ['mayo', 'mustard', 'lettuce', 'tomato']}

sandwich = []

for i,item in enumerate(ingredients.keys()):
    
    if i < 2:
        print('\nWhat kind of %s do you want?' %(item))
        sandwich += [pyip.inputMenu(ingredients[item], lettered=True)]
        
    elif i == 2:
        cheese_ask = pyip.inputYesNo('\nDo you want cheese?\n')
        if cheese_ask == 'yes':
            print('\nWhat kind of %s do you want?\n' %(item))
            sandwich += [pyip.inputMenu(ingredients[item], lettered=True)]
        else:
            sandwich += ['No cheese']
    else:
        for j, side in enumerate(ingredients['sides']):
            print('\nDo you want %s' %(side))
            if pyip.inputYesNo() == 'yes':
                sandwich += ['%s' %(side)]
            else:
                sandwich += ['No %s' %(side)]

print('\n\n')
print('Ingredients you selected'.upper())

for j, item in enumerate(sandwich):
    if j <3:
        print('%7s: %s' %(str(list((ingredients.keys()))[j]).capitalize(),str(item).capitalize()))
    else:
        print('Sides-%s: %s' %(j-2, str(item).capitalize()))

sandwichNum = pyip.inputInt('\nHow many sandwich do you want?\n', min=1)
