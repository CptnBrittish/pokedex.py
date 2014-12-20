#!/usr/bin/env python

import pykemon
import sys
import requests
from tkinter import *
from PIL import Image, ImageTk
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.grid()
        self.createWidgets()

    def createWidgets(self):
        pokemon = get_pokemon(sys.argv[1])
        pokemon_sprite = get_sprite(pokemon.id)

        sprite_file = open('temp.jpg', 'wb')
        sprite_url = requests.get('http://pokeapi.co/'+pokemon_sprite.image).content
        sprite_file.write(sprite_url)
        sprite_file.close()

        image = Image.open('temp.jpg')
        sprite = ImageTk.PhotoImage(image)
        self.poke_sprite_display = Canvas(width=120, height=120, bg='white')
        self.poke_sprite_display.create_image(60, 40, image=sprite)
        self.poke_sprite_display.image = sprite
        self.poke_sprite_display.grid(column=0, row=0)
        
        self.pokemon_name_label = Label(text="Pokemon Name:")
        self.pokemon_name_label.grid(column=1, row=0)
        self.pokemon_name = Label(text=pokemon.name)
        self.pokemon_name.grid(column=2, row=0)
        

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
    app = Application(root)
    app.master.title('Pokedex')
    app.mainloop()
