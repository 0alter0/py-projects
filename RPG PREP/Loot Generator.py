import random
#modifiers pool

#the bar thing
bar = "--------------------------------------------------------------------------------"

item_material = ["Wooden","Iron","Diamond","Crystal","Amythest","Gold","Emerald","Ruby"]
item_type = ["Sword","Axe","Dagger"]
modifiers_pool = ["Flaming","Frozen","Void","Molten","Swift","Heavy","Sharp","Holy","Ancient","Unstable","Reinforced","Venomous"]
rarities = ["Common","Uncommon","Rare","Epic","Legendary","Mythic"]

print()
print(bar)
print()

while True:
    action = input("Add a new item stat or generate a new item? [add/new] ").lower()
    print()


    if action == "new":
        while True:
            roll = input("Roll? [y/n] ").lower()
            print()

            if roll == "y":
                #dfines what the attribute values are
                rarity = random.choice(rarities)
                material = random.choice(item_material)
                itype = random.choice(item_type)

                print(bar)
                print()

                #some rarities get different modifier amounts
                if rarity == "Common":
                    mod_count = 0

                elif rarity == "Uncommon":
                    mod_count = 0

                elif rarity == "Rare":
                    mod_count = random.randint(0,1)

                elif rarity == "Epic":
                    mod_count = random.randint(0,1)

                elif rarity == "Legendary":
                    mod_count = 1

                elif rarity == "Mythic":
                    mod_count = 2

                chosen_modifiers = random.sample(modifiers_pool, k=mod_count)

                damage = 5
                price = 0
                coins = 0

                if len(chosen_modifiers) == 1:
                    damage += 10
                    price += 100

                elif len(chosen_modifiers) > 1:
                    damage += 20
                    price += 300

                if rarity == "Common":
                    damage += 2
                    price += 20

                elif rarity == "Uncommon":
                    damage += 5
                    price += 50
                
                elif rarity == "Rare":
                    damage += 10
                    price += 100

                elif rarity == "Epic":
                    damage += 15
                    price += 200

                elif rarity == "Legendary":
                    damage += 20
                    price += 300

                elif rarity == "Mythic":
                    damage += 30
                    price += 500

                #prints out the itewm names
                print(f"Rarity: {rarity}")
                print()
                print(f"Modifiers: {chosen_modifiers}")
                print()
                print(f"Item: {material} {itype}")
                print()
                print(f"Full Name: {' '.join(chosen_modifiers)} {material} {itype} ({rarity})")
                print()
                print("Damage:",damage)
                print()
                print("Price:",price)
                print()

                print(bar)
                print()

            else:
                print(bar)
                print()
                break

    elif action == "add":
            while True:
                change = input("What list would you like to add to? [material/rarity/items/modifiers/exit] ").lower()
                print()

                if change == "material":
                    change_material = input("What material would you like to add? ")
                    item_material.append(change_material)
                    print()
                    print(bar)
                    print()

                elif change == "items":
                    change_item = input("What new item would you like to add? ")
                    item_type.append(change_item)
                    print()
                    print(bar)
                    print()

                elif change == "rarity":
                    change_rarity = input("What rarity would you like to add? ")
                    rarities.append(change_rarity)
                    print()
                    print(bar)
                    print()

                elif change == "modifiers":
                    change_modifier = input("What modifier would you like to add? ")
                    modifiers_pool.append(change_modifier)
                    print()
                    print(bar)
                    print()

                elif change == "exit":
                    print(bar)
                    print()
                    break

                else:
                    print("Unknown stat, try again")
                    print()