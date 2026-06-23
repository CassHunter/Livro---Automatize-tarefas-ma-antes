stuff = {'rope':1, 'torch':6, 'gold coin':42, 'dagger':1, 'arrow':12}

def displayInventory(inventory):
    print()
    print('-------Inventory:-------')
    item_total = 0
    for k, v in inventory.items():
        print(f'{v:2} - {k}')
        item_total += v
    print(f'Total number of items:{item_total}')
    print('------------------------')
    print()

displayInventory(stuff)