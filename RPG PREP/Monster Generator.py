import random

monsters = [
    "Wolf",
    "Dire Wolf",
    "Goblin",
    "Goblin Scout",
    "Goblin Warrior",
    "Goblin Archer",
    "Rat",
    "Giant Rat",
    "Boar",
    "Wild Bear",
    "Bandit",
    "Skeleton",
    "Zombie",
    "Slime",
    "Giant Spider",
    "Bat",
    "Giant Bat",
    "Scorpion",
    "Cave Crawler",
    "Swamp Leech"
]

difficulties = ["Harmless","Dangerous","Powerful"]
mods = ["Slow","Icy","Flame","Void"]

monster_type = random.choice(monsters)
monster_health = 5
monster_damage = 5

difficulty = random.choice(difficulties)
mod = random.choice(mods)

if mod == "slow":
    monster_damage -= 5
    monster_health += 30

elif mod == "Void":
    monster_damage += 10
    monster_health += 50

else:
    monster_damage += 5
    monster_health += 20

if difficulty == "Harmless":
    monster_health += 0

elif difficulty == "Dangerous":
    monster_health += 20

else:
    monster_health += 50

print("Mob:",difficulty,mod,monster_type)
print("Health:",monster_health)
print("Damage:",monster_damage)