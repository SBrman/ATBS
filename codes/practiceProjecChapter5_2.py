import pprint
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

players_stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def addToInventory(inventory, addedItems):
    for items in addedItems:
        inventory.setdefault(items,0)
        inventory[items] += 1

    return inventory

def displayInventory(inventory):
    print('Inventory:')
    count = 0
    for k,v in inventory.items():
        print(str(v)+ ' '+ k)
        count += v
    print('Total number of items: '+ str(count))
    
inv = addToInventory(players_stuff, dragonLoot)
displayInventory(inv)
