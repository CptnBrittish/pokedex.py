#!/usr/bin/env python

import pykemon
import sys

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
    print("Stats:")
    print("\tHP: "  + str(pokemon.hp))
    print("\tAttack: " + str(pokemon.attack))
    print("\tDefence: " + str(pokemon.defense))
    print("\tSpecial Attack: " + str(pokemon.sp_atk))
    print("\tSpecial Defence: " + str(pokemon.sp_def))
    print("\tSpeed: " + str(pokemon.speed))
    print("Egg Cycles: " + str(pokemon.egg_cycles))
    print("EV yield: " + pokemon.ev_yield)
    print("Catch Rate: " + str(pokemon.catch_rate))
    print("Male to Female Ratio: " + str(pokemon.male_female_ratio))
    print("Moves: ")
    for moves in pokemon.moves:
        print("\t" + moves)

    
if sys.argv[1] == "pokemon":
    get_pokemon(sys.argv[2])
    
elif sys.argv[1] == "type":
    print("Searching for " + sys.argv[2]  + "...")
    poke_type = pykemon.get(type_id=sys.argv[2])
    print("Name: " + poke_type.name)
    if len(poke_type.super_effective) > 0:
        print("Super Effective Against:")
        for strong in poke_type.super_effective:
            print("\t" + strong)
    if len(poke_type.ineffective) > 0:
        print("Inefective against:")
        for ineffective in poke_type.ineffective:
            print("\t" + ineffective)
    if len(poke_type.resistance) > 0:
        print("Resistant to:")
        for resist in poke_type.resistance:
            print("\t" + resist)
    if len(poke_type.weakness) > 0:
        print("Weak to:")
        for weak in poke_type.weakness:
           print("\t" + weak)

elif sys.argv[1] == "move":
    print("Searching for move " + sys.argv[2] + "...")
    poke_move = pykemon.get(move_id=sys.argv[2])
    print("Name: " + poke_move.name)
    print("Accuracy: " + str(poke_move.accuracy))
    if len(poke_move.category) > 0:
        print("Category: " + str(poke_move.category))
    print("Power: " + str(poke_move.power))
    print("PP: " + str(poke_move.pp))

elif sys.argv[1] == "ability":
    print("Searching for ability " + sys.argv[2] + "..")
    poke_ability = pykemon.get(ability_id=sys.argv[2])
    print("Name: " + poke_ability.name)
    print("Description: " + poke_ability.description)
           
else:
    get_pokemon(sys.argv[1])
