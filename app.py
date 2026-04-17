import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)

print (data)
# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.

# Add a language choice feature and print the pokemons name based on the user input

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user

#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 

y = input ("What language would you like to search in?")
for letter in y:
    if letter == "E":
        print 
    if letter == "J":
        print
    if letter == "C":
        print
    if letter == "F":
        print
x = input("What pokemon would you like to find?")
for pokedex_character in data["name"]:
    print (pokedex_character)
for character in x:
    if character == pokedex_character:
        print (x)  
x = [0,1]
x = [0]
print(x)