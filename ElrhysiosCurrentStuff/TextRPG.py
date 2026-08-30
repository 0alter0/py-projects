import random
#all the variables
gold = 25
health = 100
level = 1
weapons = "sword"
attack_damage = 10 * level
kills = 0
inventory = []
loot = ["wooden sword", "stone axe", "iron sword"]
healingpots = 0
monsters = ["skeleton", "zombie", "spider"]
#beginning text banner
print()

print("--------------\n  PYTHON RPG  \n--------------")

print()

print("You wake up in a small village.")
print()
print("Gold:",gold)
print()

while True:
    #user chooses what to do
    action = input("What do you want to do?\n\n1. Explore\n2. Shop\n3. Inventory\n4. Stats\n5. Exit\n6. Items\n\n").lower()
#stops the game
    if action == "exit" or action == "5":
        print("Bye!")
        break
#randomly chooses monster attributes
    elif action == "1":
        monster_health = random.randint(20, 50)
        monster_damage = random.randint(3, 12)
        monster = random.choice(monsters)

        print()
        print("A", monster, "appeared!")

        while True:
            fight = input("What will you do?\n\n1. Attack 2. Run\n\n").lower()
            print()

            if fight == "1":
                print("You dealt", attack_damage, "damage")
                monster_health -= attack_damage

                if monster_health <= 0:
                    print("You slayed the", monster + "!")
                    gold += 25
                    kills += 1
                    print("The monster dropped 25 gold, and an item!")
                    print()
                    print("Gold:", gold)

                    new_item = random.choice(loot)
                    inventory.append(new_item)

                    print()
                    print("Your new inventory:", inventory)
                    break

                else:
                    health -= monster_damage
                    print("The monster dealt", monster_damage, "damage")
                    print("Monster HP:", monster_health)
                    print("Your HP:", health)

                    if health <= 0:
                        print("You died!")
                        break

            elif fight == "2":
                run_damage = random.randint(1, 10)
                health -= run_damage
                print("You ran away, but the monster dealt", run_damage, "damage as you ran away.")
                print("Your HP:", health)

                if health <= 0:
                    print("You died!")

                break

            else:
                print("Invalid input.")

        print()

    elif action == "3":
        try:
            print()
            print("This is your inventory:", inventory)
            delete = input("Would you like to delete anything? [y/n] ").lower()
            print()

            if delete == "y":
                itemremoved = input("What item would you like to delete? ").lower()
                inventory.remove(itemremoved)

                print()
                print("You deleted your item and gained some gold!")
                gold += random.randint(5, 20)

                print()
                print("You have", gold, "gold now.")
                print("This is your inventory now:", inventory)
                print()

            elif delete == "n":
                print()

        except ValueError:
            print("Try again, invalid input\n\n")
#lists all of the users stuff
    elif action == "4":
        print()
        print("Level:", level)
        print("Weapon:", weapons)
        print("Attack damage:", attack_damage)
        print("You have", kills, "kill(s)")
        print("Health:", health)
        print("Gold:", gold)
        print()

    elif action == "2":
        print()

        purchase = input("What would you like to buy? [Healing potion (20 gold) / Level up (50 gold)/exit] ").lower()

        if purchase == "healing potion":
            if gold >= 20:
                gold -= 20
                healingpots += 1

                print()
                print("You now have", healingpots, "healing potions")
                print("You now have", gold, "gold")
            else:
                print("Not enough gold.")

        elif purchase == "level" or purchase == "level up":
            if gold >= 50:
                gold -= 50
                level += 1
                attack_damage += 5

                print()
                print("You now have", gold, "gold")
                print("You are now level", level)
                print("Your attack damage is now", attack_damage)

            elif purchase == "exit":
                break

            else:
                print("Not enough money")

        else:
            print("Invalid purchase.")

    elif action == "6":
        print()
        print(healingpots, "health potions")
        print()

        useitem = input("Do you want to use an item? [y/n] ").lower()

        if useitem == "y":
            itemused = input("What item? ").lower()

            if itemused == "health potion":
                if healingpots > 0:
                    if health < 100:
                        health = min(health + 50, 100)
                        healingpots -= 1

                        print("Health:", health)
                        print("Health potions:", healingpots)
                    else:
                        print("Your health is already full.")
                else:
                    print("You don't have any healing potions.")

            else:
                print("You don't have that item.")

        elif useitem == "n":
            print("Leaving...")
            print()

        else:
            print("Invalid input.")

    else:
        print("Invalid input.")      
