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
        self.createWidgets()

    def createPokemonWidgets(self, pokemon_to_serch):
        self.pokemon_frame = Frame()
        self.pokemon_frame.grid(column = 0, row = 1)
        pokemon = get_pokemon(pokemon_to_serch)
        pokemon_sprite = get_sprite(pokemon.id)

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
        self.poke_sprite_display.grid(column=0, row=0, rowspan = 8)
        
        self.pokemon_name_label = Label(self.pokemon_frame, text="Pokemon Name:")
        self.pokemon_name_label.grid(column=1, row=0)
        self.pokemon_name = Label(self.pokemon_frame, text=pokemon.name)
        self.pokemon_name.grid(column=2, row=0)

        self.pokemon_type_label = Label(self.pokemon_frame, text="Types:", anchor=S)
        self.pokemon_type_label.grid(column=1, row=1)
        pokemon_types = str()
        
        poke_types = list(pokemon.types)
        pokemon_types = poke_types[0]
        for type in poke_types[1:]:
            pokemon_types = pokemon_types + ", " +  type
        self.pokemon_type = Label(self.pokemon_frame, text=pokemon_types)
        self.pokemon_type.grid(column=2, row=1)
        
    def createWidgets(self):
        self.search_frame = Frame()
        self.search_frame.grid(column=0, row=0)
        self.search_term = Entry(self.search_frame)
        self.search_term.grid(column=0, row=0)
        self.search_button = Button(self.search_frame, text='Search', command=lambda: self.createPokemonWidgets(self.search_term.get()))
        self.search_button.grid(column=1, row=0)
        
    
        

def get_pokemon(poke_name):
    print("Searching for " + poke_name + "...")
    pokemon = pykemon.get(pokemon=poke_name)
    print("Pokemon found, retreiving information...")
    return pokemon

def get_sprite(poke_num):
    pokemon_sprite = pykemon.get(sprite=poke_num)
    return pokemon_sprite


if __name__ == "__main__":
    root = Tk()
    img = PhotoImage(file='pokeball.png')
    root.tk.call('wm', 'iconphoto', root._w, img)
    app = Application(root)
    app.master.title('Pokedex')
    app.mainloop()
