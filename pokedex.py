#!/usr/bin/env python

import pykemon
import sys
import requests

from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.grid()
        
        self.search_frame = Frame()
        self.search_frame.grid(column = 0, row = 0)
        self.content_frame = Frame()
        self.content_frame.grid(column = 0, row = 1)

        self.is_pokemon_searched = 0
        
        self.createWidgets()

    def has_pokemon_been_searched(self, pokemon):
        if self.is_pokemon_searched == 1:
            self.content_frame.grid_forget()
        self.is_pokemon_searched = 1
        self.content_frame.grid(column = 0, row = 1)
        self.createPokemonWidgets(pokemon)
                

    def createPokemonWidgets(self, pokemon_to_search):
        self.pokemon_frame = Frame(self.content_frame)
        self.pokemon_frame.grid(column = 0, row = 1)
        pokemon = get_pokemon(pokemon_to_search)
        pokemon_sprite = get_sprite(pokemon.sprites[sorted(pokemon.sprites.keys())[0]][15:-1])

        sprite_file = open('temp.jpg', 'wb')
        sprite_url = requests.get('http://pokeapi.co/'+pokemon_sprite.image).content
        sprite_file.write(sprite_url)
        sprite_file.close()

        #make sure all sprites are the same size
        img = Image.open('temp.jpg')
        size = 120, 120
        img.thumbnail(size)
        img.save('temp.png', "PNG")
        
        image = Image.open('temp.png')
        sprite = ImageTk.PhotoImage(image)

        self.poke_sprite_display = Canvas(self.pokemon_frame, width=120, height=120, bg='white')
        self.poke_sprite_display.create_image(60, 60, image=sprite)
        self.poke_sprite_display.image = sprite
        self.poke_sprite_display.grid(column=0,columnspan=4, row=0, rowspan = 11)

        #Pokemon name
        self.pokemon_name_label = Label(self.pokemon_frame, text="Name:")
        self.pokemon_name_label.grid(column=0, row=9)
        self.pokemon_name = Label(self.pokemon_frame, text=pokemon.name)
        self.pokemon_name.grid(column=1, row=9)

        #pokemon gender
        self.pokemon_gender_label = Label(self.pokemon_frame, text="Gender:")
        self.pokemon_gender_label.grid(column=0, row=10)

        #pokemon national id
        self.pokemon_number_label = Label(self.pokemon_frame, text="#")
        self.pokemon_number_label.grid(column=3, row=10)
        self.pokemon_number = Label(self.pokemon_frame, text=pokemon.id)
        self.pokemon_number.grid(column = 4, row = 10)

        #Pokemon types
        self.pokemon_type_label = Label(self.pokemon_frame, text="Type:", anchor=S)
        self.pokemon_type_label.grid(column=5, row=0)
        pokemon_types = str()
        
        poke_types = list(pokemon.types)
        pokemon_types = poke_types[0]
        for type in poke_types[1:]:
            pokemon_types = pokemon_types + ", " +  type
        self.pokemon_type = Label(self.pokemon_frame, text=pokemon_types)
        self.pokemon_type.grid(column=6, row=0)

        #Pokemon Species
        self.pokemon_species_label = Label(self.pokemon_frame, text="Species:")
        self.pokemon_species_label.grid(column=5, row=1)
        self.pokemon_species = Label(self.pokemon_frame, text=pokemon.species)
        self.pokemon_species.grid(column=6, row=1)

        #height and weight
        self.pokemon_height_label = Label(self.pokemon_frame, text="Height:")
        self.pokemon_height_label.grid(column=5, row=2)
        self.pokemon_height = Label(self.pokemon_frame, text=pokemon.height)
        self.pokemon_height.grid(column=6, row=2)
        self.pokemon_weight_label = Label(self.pokemon_frame, text="Weight:")
        self.pokemon_weight_label.grid(column=7, row=2)
        self.pokemon_weight = Label(self.pokemon_frame, text=pokemon.weight)
        self.pokemon_weight.grid(column=8, row=2)

        #Pokemon Abilities
        self.pokemon_abilities_label = Label(self.pokemon_frame, text="Abilities:")
        self.pokemon_abilities_label.grid(column=5, row=3)
        self.pokemon_abilities = Label(self.pokemon_frame, text=pokemon.abilities)

        #Pokemon weaknesses
        self.pokemon_weaknesses_label = Label(self.pokemon_frame, text="Weaknesses:")
        self.pokemon_weaknesses_label.grid(column=5, row=4)

        #Stats
        self.pokemon_hp_label = Label(self.pokemon_frame, text="HP")
        self.pokemon_hp_label.grid(column=5, row=5)
        self.pokemon_defense_label = Label(self.pokemon_frame, text="Defense")
        self.pokemon_defense_label.grid(column=5, row=7)
        self.pokemon_attack_label = Label(self.pokemon_frame, text="Attack")
        self.pokemon_attack_label.grid(column=5, row=9)
        self.pokemon_speed_label = Label(self.pokemon_frame, text="Speed")
        self.pokemon_speed_label.grid(column=6, row=5)
        self.pokemon_sp_defense_label = Label(self.pokemon_frame, text="Sp Defense")
        self.pokemon_sp_defense_label.grid(column=6, row=7)
        self.pokemon_sp_attack_label = Label(self.pokemon_frame, text="Sp Attack")
        self.pokemon_sp_attack_label.grid(column=6, row=9)
        
        #description
        self.pokemon_description = Label(self.pokemon_frame, text=get_description(pokemon.descriptions[sorted(pokemon.descriptions.keys())[0]][20:-1]).description, wraplength=160)
        self.pokemon_description.grid(column=5, row=10, columnspan=4, rowspan=4)
        
    def createWidgets(self):
        self.search_term = Entry(self.search_frame)
        self.search_term.grid(column=0, row=0)
        self.search_button = Button(self.search_frame, text='Search', command=lambda: self.has_pokemon_been_searched(self.search_term.get()))
        self.search_term.bind("<Return>", lambda event: self.has_pokemon_been_searched(self.search_term.get()))
        self.search_button.grid(column=1, row=0)
        
    
        

def get_pokemon(poke_name):
    print("Searching for " + poke_name + "...")
    pokemon = pykemon.get(pokemon=poke_name)
    print("Pokemon found, retreiving information...")
    return pokemon

def get_sprite(poke_num):
    pokemon_sprite = pykemon.get(sprite=poke_num)
    return pokemon_sprite

def get_description(poke_des):
    pokemon_description = pykemon.get(description=poke_des)
    return pokemon_description

if __name__ == "__main__":
    root = Tk()
    img = PhotoImage(file='pokeball.png')
    root.tk.call('wm', 'iconphoto', root._w, img)
    app = Application(root)
    app.master.title('Pokedex')
    app.mainloop()
