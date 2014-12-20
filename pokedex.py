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

        #make sure all sprites are the same size
        img = Image.open('temp.jpg')
        size = 120, 120
        img.thumbnail(size)
        img.save('temp', "JPEG")
        
        image = Image.open('temp.jpg')
        sprite = ImageTk.PhotoImage(image)

        self.poke_sprite_display = Canvas(width=120, height=120, bg='white')
        self.poke_sprite_display.create_image(60, 60, image=sprite)
        self.poke_sprite_display.image = sprite
        self.poke_sprite_display.grid(column=0, row=0, rowspan = 8)
        
        self.pokemon_name_label = Label(text="Pokemon Name:")
        self.pokemon_name_label.grid(column=1, row=0)
        self.pokemon_name = Label(text=pokemon.name)
        self.pokemon_name.grid(column=2, row=0)

        self.pokemon_type_label = Label(text="Types:", anchor=S)
        self.pokemon_type_label.grid(column=1, row=1)
        pokemon_types = str()
        
        poke_types = list(pokemon.types)
        pokemon_types = poke_types[0]
        for type in poke_types[1:]:
            pokemon_types = pokemon_types + ", " +  type
        self.pokemon_type = Label(text=pokemon_types)
        self.pokemon_type.grid(column=2, row=1)
        

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
