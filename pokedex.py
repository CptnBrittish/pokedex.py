#!/usr/bin/env python

import pykemon
import sys
import ast

def get_pokemon(poke_name):
    print("Searching for " + poke_name + "...")
    pokemon = pykemon.get(pokemon=poke_name)
    print("Pokemon found, retreiving information...")
    poke_description=pykemon.get(description_id=pokemon.descriptions.get(list(pokemon.descriptions.keys())[0])[20:-1])

    print("Name: " + pokemon.name)
    print("National Pokedex Number: " + str(pokemon.id))
    print("Description: " + poke_description.description)

    print("Types: ")
    for types in pokemon.types:
        print("\t" + types)
    if len(pokemon.evolutions) > 0:
        print("Evolution: ")
        for evolution in pokemon.evolutions:
            print("\t" + evolution)
    else:
        print("This pokemon has no evolutions")
    print("Catch Rate: " + str(pokemon.catch_rate))
    print("Male to Female Ratio: " + str(pokemon.male_female_ratio))
    print("Moves: ")
    for moves in pokemon.moves:
        print("\t" + moves)

    
if sys.argv[1] == "pokemon":
    get_pokemon(sys.argv[2])
else:
    get_pokemon(sys.argv[1])
