import random

adjectives = [
    "Stealth", "Phantom", "Iron", "Viper", "Raven",
    "Blazing", "Spectral", "Vulcan", "Cerberus", "Obsidian",
    "Thunder", "Frost", "Scarlet", "Deadly", "Crimson",
    "Lone", "Shadow", "Nuclear", "Tactical", "Black"
]

animals = [
    "Fox", "Ocelot", "Wolf", "Raven", "Mantis",
    "Cobra", "Bear", "Hound", "Viper", "Scorpion",
    "Hornet", "Tiger", "Rhino", "Condor", "Python",
    "Wasp", "Jackal", "Octopus", "Eagle", "Spider"
]
def print_codename(name, adjective, animal):
    print(f"{name}, your codename is: {adjective} {animal}")
print("What is your name?")
name = input()
animal = random.choice(animals)
adjective = random.choice(adjectives)
print_codename(name, adjective, animal)
print("Your lucky number is: " + str(random.randint(1, 99)))