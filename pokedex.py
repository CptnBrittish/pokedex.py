#!/usr/bin/env python

import os
import requests
import get_pokemon_information

from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk
from PIL import Image


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.grid()
        
        self.search_frame = Frame()
        self.search_frame.grid(column = 0, row = 0)
        self.content_frame = Frame()
        self.content_frame.grid(column = 0, row = 1)

        self.pokemon_data = self.pokemon_data()
        self.poke_info = get_pokemon_information.pokemon_information()
        self.createPokemonWidgets()
        self.createWidgets()

    class pokemon_data:
        def __init__(self):
            self.sprite = ImageTk.PhotoImage(Image.new("RGBA", (120,120), 'White'))
            self.pokemon_name_var = StringVar()
            self.pokemon_gender_var = StringVar()
            self.pokemon_number_var = StringVar()
            self.pokemon_types_var = StringVar()
            self.pokemon_species_var = StringVar()
            self.pokemon_height_var = StringVar()
            self.pokemon_weight_var = StringVar()
            self.pokemon_abilities_var = StringVar()
            self.pokemon_description_var = StringVar()
            self.pokemon_weaknesses_var = StringVar()

            self.pokemon_attack_var = StringVar()
            self.pokemon_sp_attack_var = StringVar()
            self.pokemon_defense_var = StringVar()
            self.pokemon_sp_defense_var = StringVar()
            self.pokemon_hp_var = StringVar()
            self.pokemon_speed_var = StringVar()

    def createPokemonWidgets(self):
        self.pokemon_frame = Frame(self.content_frame)
        self.pokemon_frame.grid(column = 0, row = 1)

        self.poke_sprite_display = Canvas(self.pokemon_frame, width=120, height=120, bg='white')
        self.poke_sprite_display.create_image(60, 60, image=self.pokemon_data.sprite)
        self.poke_sprite_display.image = self.pokemon_data.sprite
        self.poke_sprite_display.grid(column=0,columnspan=4, row=0, rowspan = 11)

        #Pokemon name
        self.pokemon_name_label = Label(self.pokemon_frame, text="Name:")
        self.pokemon_name_label.grid(column=0, row=11)


        self.pokemon_name = Label(self.pokemon_frame, textvariable=self.pokemon_data.pokemon_name_var)
        self.pokemon_name.grid(column=1, row=11)

        #pokemon gender
        self.pokemon_gender_label = Label(self.pokemon_frame, text="Gender Ratio:")
        self.pokemon_gender_label.grid(column=0, row=12)

        self.pokemon_gender = Label(self.pokemon_frame, textvariable=self.pokemon_data.pokemon_gender_var)
        self.pokemon_gender.grid(column=1, row=12)

        #pokemon national id
        self.pokemon_number_label = Label(self.pokemon_frame, text="#")
        self.pokemon_number_label.grid(column=3, row=12)


        self.pokemon_number = Label(self.pokemon_frame, textvariable=self.pokemon_data.pokemon_number_var)
        self.pokemon_number.grid(column = 4, row = 12)

        #Pokemon types
        self.pokemon_type_label = Label(self.pokemon_frame, text="Type:", anchor=S)
        self.pokemon_type_label.grid(column=5, row=0)
        

        self.pokemon_type = Label(self.pokemon_frame, textvariable=self.pokemon_data.pokemon_types_var)
        self.pokemon_type.grid(column=6, row=0)

        #Pokemon Species
        self.pokemon_species_label = Label(self.pokemon_frame, text="Species:")
        self.pokemon_species_label.grid(column=5, row=1)

        self.pokemon_species = Label(self.pokemon_frame, textvariable=self.pokemon_data.pokemon_species_var)
        self.pokemon_species.grid(column=6, row=1)

        #height and weight
        self.pokemon_height_label = Label(self.pokemon_frame, text="Height:")
        self.pokemon_height_label.grid(column=5, row=2)

        self.pokemon_height = Label(self.pokemon_frame, textvariable=self.pokemon_data.pokemon_height_var)
        self.pokemon_height.grid(column=6, row=2)
        
        self.pokemon_weight_label = Label(self.pokemon_frame, text="Weight:")
        self.pokemon_weight_label.grid(column=7, row=2)

        self.pokemon_weight = Label(self.pokemon_frame, textvariable=self.pokemon_data.pokemon_weight_var)
        self.pokemon_weight.grid(column=8, row=2)

        #Pokemon Abilities
        self.pokemon_abilities_label = Label(self.pokemon_frame, text="Abilities:")
        self.pokemon_abilities_label.grid(column=5, row=3)

        self.pokemon_abilities = Label(self.pokemon_frame, textvariable=self.pokemon_data.pokemon_abilities_var)
        self.pokemon_abilities.grid(column=6, row=3)

        #Pokemon weaknesses
        self.pokemon_weaknesses_label = Label(self.pokemon_frame, text="Weaknesses:")
        self.pokemon_weaknesses_label.grid(column=5, row=4)

        self.pokemon_weakness = Label(self.pokemon_frame, textvariable=self.pokemon_data.pokemon_weaknesses_var)
        self.pokemon_weakness.grid(column=6, row=4)

        #Stats
        self.pokemon_hp_label = Label(self.pokemon_frame, text="HP")
        self.pokemon_hp_label.grid(column=5, row=5)
        self.pokemon_hp = Label(self.pokemon_frame, textvariable=self.pokemon_data.pokemon_hp_var)
        self.pokemon_hp.grid(column=5, row=6)
        
        self.pokemon_defense_label = Label(self.pokemon_frame, text="Defense")
        self.pokemon_defense_label.grid(column=5, row=7)
        self.pokemon_defense = Label(self.pokemon_frame, textvariable=self.pokemon_data.pokemon_defense_var)
        self.pokemon_defense.grid(column=5, row=8)
        
        self.pokemon_attack_label = Label(self.pokemon_frame, text="Attack")
        self.pokemon_attack_label.grid(column=5, row=9)
        self.pokemon_attack = Label(self.pokemon_frame, textvariable=self.pokemon_data.pokemon_attack_var)
        self.pokemon_attack.grid(column=5, row=10)
        
        self.pokemon_speed_label = Label(self.pokemon_frame, text="Speed")
        self.pokemon_speed_label.grid(column=6, row=5)
        self.pokemon_speed = Label(self.pokemon_frame, textvariable=self.pokemon_data.pokemon_speed_var)
        self.pokemon_speed.grid(column=6, row=6)
        
        self.pokemon_sp_defense_label = Label(self.pokemon_frame, text="Sp Defense")
        self.pokemon_sp_defense_label.grid(column=6, row=7)
        self.pokemon_sp_defense = Label(self.pokemon_frame, textvariable=self.pokemon_data.pokemon_sp_defense_var)
        self.pokemon_sp_defense.grid(column=6, row=8)
        
        self.pokemon_sp_attack_label = Label(self.pokemon_frame, text="Sp Attack")
        self.pokemon_sp_attack_label.grid(column=6, row=9)
        self.pokemon_sp_attack = Label(self.pokemon_frame, textvariable=self.pokemon_data.pokemon_sp_attack_var)
        self.pokemon_sp_attack.grid(column=6, row=10)
        
        #description

        self.pokemon_description = Label(self.pokemon_frame, textvariable=self.pokemon_data.pokemon_description_var, wraplength=160)
        self.pokemon_description.grid(column=5, row=10, columnspan=4, rowspan=4)

    def updatePokemonWidgets(self, poke_name):
        pokemon = self.poke_info.get(pokemon=poke_name)

        poke_type = self.poke_info.get(type=pokemon.types[list(pokemon.types.keys())[0]][13:-1])
        sprite_info = self.poke_info.get(sprite=pokemon.sprites[list(pokemon.sprites.keys())[0]][15:-1])
        image = self.poke_info.get_sprite(sprite_info.image)
        poke_description = self.poke_info.get(description=pokemon.descriptions[sorted(pokemon.descriptions.keys())[0]][20:-1])

        self.pokemon_data.sprite.paste(image)
        self.pokemon_data.pokemon_name_var.set(pokemon.name)
        self.pokemon_data.pokemon_number_var.set(pokemon.id)

        if pokemon.male_female_ratio:
            self.pokemon_data.pokemon_gender_var.set(str(pokemon.male_female_ratio))
        else:
            self.pokemon_data.pokemon_gender_var.set("Genderless")
        
        pokemon_types = str()
        
        poke_types = list(pokemon.types)
        pokemon_types = poke_types[0]
        for type in poke_types[1:]:
            pokemon_types = pokemon_types + ", " +  type
        self.pokemon_data.pokemon_types_var.set(pokemon_types)

        pokemon_weakness = str()
        for type in list(pokemon.types.keys()):
            poke_type = self.poke_info.get(type=pokemon.types[type][13:-1])
            pokemon_weakness = list(poke_type.weakness.keys())[0]
            for weakness in list(poke_type.weakness.keys())[1:]:
                pokemon_weakness = pokemon_weakness + ", " + weakness
        self.pokemon_data.pokemon_weaknesses_var.set(pokemon_weakness)

        pokemon_abilities = list(pokemon.abilities.keys())[0]
        for abilities in list(pokemon.abilities.keys())[1:]:
            pokemon_abilities = pokemon_abilities + ", " + abilities
        self.pokemon_data.pokemon_abilities_var.set(pokemon_abilities)
        
        if pokemon.species:
            self.pokemon_data.pokemon_species_var.set(pokemon.species.title())
        else:
            self.pokemon_data.pokemon_species_var.set("New Species")
        self.pokemon_data.pokemon_height_var.set(str(pokemon.height))
        self.pokemon_data.pokemon_weight_var.set(str(pokemon.weight))
        self.pokemon_data.pokemon_description_var.set(poke_description.description)

        self.pokemon_data.pokemon_hp_var.set(str(pokemon.hp))
        self.pokemon_data.pokemon_speed_var.set(str(pokemon.speed))
        self.pokemon_data.pokemon_attack_var.set(str(pokemon.attack))
        self.pokemon_data.pokemon_sp_attack_var.set(str(pokemon.sp_atk))
        self.pokemon_data.pokemon_defense_var.set(str(pokemon.defense))
        self.pokemon_data.pokemon_sp_defense_var.set(str(pokemon.sp_def))
        
    def createWidgets(self):
        self.search_term = Entry(self.search_frame)
        self.search_term.grid(column=0, row=0)
        self.search_button = Button(self.search_frame, text='Search', command=lambda: self.updatePokemonWidgets(self.search_term.get()))
        self.search_term.bind("<Return>", lambda event: self.updatePokemonWidgets(self.search_term.get()))
        self.search_button.grid(column=1, row=0)


if __name__ == "__main__":
    if not os.path.exists("cache"):
        os.mkdir("cache")
    root = Tk()
    img = PhotoImage(file='pokeball.png')
    root.tk.call('wm', 'iconphoto', root._w, img)
    app = Application(root)
    app.master.title('Pokedex')
    app.mainloop()
