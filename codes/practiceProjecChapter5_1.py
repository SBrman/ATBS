inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(allItems):
    print('Inventory:')
    count = 0
    for k,v in allItems.items():
        print(str(v) +' '+ k)
        count += v
    print('Total number of items: '+ str(count))

displayInventory(inventory)
