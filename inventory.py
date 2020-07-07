inventory = {
    'rope': 1,
    'torch': 6,
    'gold coin': 42,
    'dagger': 1,
    'arrow': 12
}

dragonLoot = [
    'gold coin',
    'dagger',
    'gold coin',
    'gold coin',
    'ruby'
]

def displayInventory(inventory):
    print("Inventory: \n")
    for key in inventory:
        print(key, ': ', inventory[key])

def addToInventory(inventory, addedItems):
    for i in addedItems:
        if i in inventory:
            inventory[i] += 1
        else:
            inventory[i] = 1

displayInventory(inventory)
addToInventory(inventory, dragonLoot)
displayInventory(inventory)