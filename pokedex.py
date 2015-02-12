#!/usr/bin/env python3

import os
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
        self.search_frame.grid(column=0, row=0)
        self.content_frame = Frame()
        self.content_frame.grid(column=0, row=1)
        
        self.pokemon_data = self.pokemon_data()
        self.pokemon_frames = self.pokemon_frames(self.content_frame)
        self.poke_info = get_pokemon_information.pokemon_information()
        
        self.createPokemonWidgets()
        self.createWidgets()

    class pokemon_data:
        def __init__(self):
            self.sprite = ImageTk.PhotoImage(Image.new("RGBA", (120, 120), 'White'))
            self.pokemon_name_var = StringVar()
            self.pokemon_gender_var = StringVar()
            self.pokemon_number_var = StringVar()
            self.pokemon_catch_rate_var = StringVar()
            self.pokemon_types_var = StringVar()
            self.pokemon_species_var = StringVar()
            self.pokemon_height_var = StringVar()
            self.pokemon_weight_var = StringVar()
            self.pokemon_description_var = StringVar()
            self.pokemon_weaknesses_var = StringVar()

            # These are dynamically added to the number of abilities the pokemon has
            self.pokemon_abilities_var = []
            self.pokemon_abilities_description_var = []
            # This seems like a good place to put our list of labels
            self.pokemon_abilities_label = []
            self.pokemon_abilities_description_label = []

            self.pokemon_evolution_display_image = []
            self.pokemon_evolution_sprite = []
            self.pokemon_evolution_name = []

            
            self.pokemon_attack_var = StringVar()
            self.pokemon_sp_attack_var = StringVar()
            self.pokemon_defense_var = StringVar()
            self.pokemon_sp_defense_var = StringVar()
            self.pokemon_hp_var = StringVar()
            self.pokemon_speed_var = StringVar()

            self.pokemon_growth_rate_var = StringVar()
            self.pokemon_egg_cycles_var = StringVar()
            self.pokemon_egg_group_var = StringVar()

    class pokemon_frames(Frame):
        def __init__(self, content_frame):
            self.content_frame = content_frame
            self.pokemon_frame = Frame(self.content_frame)
            self.pokemon_frame.grid(column=0, row=1)
            self.abilities_frame = Frame(self.pokemon_frame)
            self.abilities_frame.grid(column=1, row = 4)
            self.basic_info_frame = Frame(self.pokemon_frame)
            self.basic_info_frame.grid(column=0, row=0)
            self.description_frame = Frame(self.pokemon_frame)
            self.description_frame.grid(column=0, row=1)
            self.stats_frame = Frame(self.pokemon_frame)
            self.stats_frame.grid(column=1, row=1)
            self.evolution_frame = Frame(self.pokemon_frame)
            self.evolution_frame.grid(column=0, columnspan=2, row=3)
            self.egg_frame = Frame(self.pokemon_frame)
            self.egg_frame.grid(column=0, row=4)

    def createPokemonWidgets(self):

        
        # Pokemon name
        self.pokemon_name_label = Label(self.pokemon_frames.basic_info_frame, text="Name:", width=12)
        self.pokemon_name_label.grid(column=0, row=0)

        self.pokemon_name = Label(self.pokemon_frames.basic_info_frame, textvariable=self.pokemon_data.pokemon_name_var, width=12)
        self.pokemon_name.grid(column=1, row=0)


        # Pokemon national id
        self.pokemon_number_label = Label(self.pokemon_frames.basic_info_frame, text="National Id:", width=12)
        self.pokemon_number_label.grid(column=0, row=1)

        self.pokemon_number = Label(self.pokemon_frames.basic_info_frame, textvariable=self.pokemon_data.pokemon_number_var, width=12)
        self.pokemon_number.grid(column=1, row=1)

        # Pokemon Species
        self.pokemon_species_label = Label(self.pokemon_frames.basic_info_frame, text="Species:", width=12)
        self.pokemon_species_label.grid(column=0, row=2)

        self.pokemon_species = Label(self.pokemon_frames.basic_info_frame, textvariable=self.pokemon_data.pokemon_species_var, width=12)
        self.pokemon_species.grid(column=1, row=2)

        # Pokemon gende ratio
        self.pokemon_gender_label = Label(self.pokemon_frames.basic_info_frame, text="Gender Ratio:", width=12)
        self.pokemon_gender_label.grid(column=0, row=4)

        self.pokemon_gender = Label(self.pokemon_frames.basic_info_frame, textvariable=self.pokemon_data.pokemon_gender_var, width=12)
        self.pokemon_gender.grid(column=1, row=4)

        self.pokemon_catch_rate_label = Label(self.pokemon_frames.basic_info_frame, text="Catch Rate:", width=12)
        self.pokemon_catch_rate_label.grid(column=0, row=5)
        self.pokemon_catch_rate = Label(self.pokemon_frames.basic_info_frame, textvariable=self.pokemon_data.pokemon_catch_rate_var, width=12)
        self.pokemon_catch_rate.grid(column=1, row=5)

        
        # Pokemon Sprite
        self.poke_sprite_display = Canvas(self.pokemon_frames.pokemon_frame, width=120, height=120, bg='white')
        self.poke_sprite_display.create_image(60, 60, image=self.pokemon_data.sprite)
        self.poke_sprite_display.image = self.pokemon_data.sprite
        self.poke_sprite_display.grid(column=1, row=0)


        self.description = Label(self.pokemon_frames.description_frame, text="Description")
        self.description.grid(column=0, row=0, columnspan=2)

        # Height and Weight
        self.pokemon_height_label = Label(self.pokemon_frames.description_frame, text="Height:")
        self.pokemon_height_label.grid(column=0, row=1)

        self.pokemon_height = Label(self.pokemon_frames.description_frame, textvariable=self.pokemon_data.pokemon_height_var, width=19)
        self.pokemon_height.grid(column=1, row=1)

        self.pokemon_weight_label = Label(self.pokemon_frames.description_frame, text="Weight:")
        self.pokemon_weight_label.grid(column=0, row=2)

        self.pokemon_weight = Label(self.pokemon_frames.description_frame, textvariable=self.pokemon_data.pokemon_weight_var, width=19)
        self.pokemon_weight.grid(column=1, row=2)

        # Description

        self.pokemon_description = Label(self.pokemon_frames.description_frame, textvariable=self.pokemon_data.pokemon_description_var, wraplength=170)
        self.pokemon_description.grid(column=0, row=3, columnspan=2, rowspan=8)

        # Stats
        self.pokemon_hp_label = Label(self.pokemon_frames.stats_frame, text="HP", width=10)
        self.pokemon_hp_label.grid(column=0, row=0)
        self.pokemon_hp = Label(self.pokemon_frames.stats_frame, textvariable=self.pokemon_data.pokemon_hp_var)
        self.pokemon_hp.grid(column=1, row=0)

        self.pokemon_attack_label = Label(self.pokemon_frames.stats_frame, text="Attack", width=10)
        self.pokemon_attack_label.grid(column=0, row=1)
        self.pokemon_attack = Label(self.pokemon_frames.stats_frame, textvariable=self.pokemon_data.pokemon_attack_var)
        self.pokemon_attack.grid(column=1, row=1)

        self.pokemon_defense_label = Label(self.pokemon_frames.stats_frame, text="Defense",width=10)
        self.pokemon_defense_label.grid(column=0, row=2)
        self.pokemon_defense = Label(self.pokemon_frames.stats_frame, textvariable=self.pokemon_data.pokemon_defense_var)
        self.pokemon_defense.grid(column=1, row=2)

        self.pokemon_sp_attack_label = Label(self.pokemon_frames.stats_frame, text="Sp Attack", width=10)
        self.pokemon_sp_attack_label.grid(column=0, row=3)
        self.pokemon_sp_attack = Label(self.pokemon_frames.stats_frame, textvariable=self.pokemon_data.pokemon_sp_attack_var)
        self.pokemon_sp_attack.grid(column=1, row=3)

        self.pokemon_sp_defense_label = Label(self.pokemon_frames.stats_frame, text="Sp Defense",width=10)
        self.pokemon_sp_defense_label.grid(column=0, row=4)
        self.pokemon_sp_defense = Label(self.pokemon_frames.stats_frame, textvariable=self.pokemon_data.pokemon_sp_defense_var)
        self.pokemon_sp_defense.grid(column=1, row=4)

        self.pokemon_speed_label = Label(self.pokemon_frames.stats_frame, text="Speed", width=10)
        self.pokemon_speed_label.grid(column=0, row=5)
        self.pokemon_speed = Label(self.pokemon_frames.stats_frame, textvariable=self.pokemon_data.pokemon_speed_var)
        self.pokemon_speed.grid(column=1, row=5)


        # Evolutions
        self.evolution_label = Label(self.pokemon_frames.evolution_frame, text="Evolutions", background='green')
        self.evolution_label.grid(row=0, sticky=W+E)


        self.pokemon_growth_rate_label = Label(self.pokemon_frames.egg_frame, text="Growth Rate:", width=12)
        self.pokemon_growth_rate_label.grid(column=0, row =0)
        self.pokemon_growth_rate = Label(self.pokemon_frames.egg_frame, textvariable=self.pokemon_data.pokemon_growth_rate_var, width=17)
        self.pokemon_growth_rate.grid(column=1, row=0)

        self.pokemon_egg_cycles_label = Label(self.pokemon_frames.egg_frame, text="Egg Cycles:",width=12)
        self.pokemon_egg_cycles_label.grid(column=0, row=1)
        self.pokemon_egg_cycles = Label(self.pokemon_frames.egg_frame, textvariable=self.pokemon_data.pokemon_egg_cycles_var, width=17)
        self.pokemon_egg_cycles.grid(column=1, row=1)

        self.pokemon_egg_group_label = Label(self.pokemon_frames.egg_frame, text="Egg Group:", width=12)
        self.pokemon_egg_group_label.grid(column=0, row=2)
        self.pokemon_egg_group = Label(self.pokemon_frames.egg_frame, textvariable=self.pokemon_data.pokemon_egg_group_var, width=17)
        self.pokemon_egg_group.grid(column=1, row=2)

        # Pokemon Abilities
        self.pokemon_abilities_label = Label(self.pokemon_frames.abilities_frame, text="Abilities")
        self.pokemon_abilities_label.grid(column=0, row=0, columnspan=2)



        '''
        # Pokemon types
        self.pokemon_type_label = Label(self.pokemon_frame, text="Type:", anchor=S)
        self.pokemon_type_label.grid(column=5, row=0)

        self.pokemon_type = Label(self.pokemon_frame, textvariable=self.pokemon_data.pokemon_types_var)
        self.pokemon_type.grid(column=6, row=0)


        

        # Pokemon weaknesses
        self.pokemon_weaknesses_label = Label(self.pokemon_frame, text="Weaknesses:")
        self.pokemon_weaknesses_label.grid(column=5, row=4)

        self.pokemon_weakness = Label(self.pokemon_frame, textvariable=self.pokemon_data.pokemon_weaknesses_var)
        self.pokemon_weakness.grid(column=6, row=4)
        
        
        '''
        

    def updatePokemonWidgets(self, poke_name):
        pokemon = self.poke_info.get(pokemon=poke_name)

        poke_type = self.poke_info.get(type=pokemon.types[list(pokemon.types.keys())[0]][13:-1])
        try:
            sprite_info = self.poke_info.get(sprite=pokemon.sprites[sorted(pokemon.sprites.keys())[-1]][15:-1])
            image = self.poke_info.get_sprite(sprite_info.image)
        except IndexError:
            print("No sprite avaiable")
        poke_description = self.poke_info.get(description=pokemon.descriptions[sorted(pokemon.descriptions.keys())[0]][20:-1])

        self.pokemon_data.sprite.paste(image)
        self.pokemon_data.pokemon_name_var.set(pokemon.name)
        self.pokemon_data.pokemon_number_var.set(pokemon.id)
        self.pokemon_data.pokemon_catch_rate_var.set(str(pokemon.catch_rate))

        if pokemon.male_female_ratio:
            self.pokemon_data.pokemon_gender_var.set(str(pokemon.male_female_ratio))
        else:
            self.pokemon_data.pokemon_gender_var.set("Genderless")

        pokemon_types = str()

        poke_types = list(pokemon.types)
        pokemon_types = poke_types[0]
        for type in poke_types[1:]:
            pokemon_types = pokemon_types + ", " + type
        self.pokemon_data.pokemon_types_var.set(pokemon_types)

        pokemon_weakness = str()
        for type in list(pokemon.types.keys()):
            poke_type = self.poke_info.get(type=pokemon.types[type][13:-1])
            pokemon_weakness = list(poke_type.weakness.keys())[0]
            for weakness in list(poke_type.weakness.keys())[1:]:
                pokemon_weakness = pokemon_weakness + ", " + weakness
        self.pokemon_data.pokemon_weaknesses_var.set(pokemon_weakness)

        # First destroy any old labels
        i = 0
        for abilities in self.pokemon_data.pokemon_abilities_var:
            self.pokemon_data.pokemon_abilities_label[i].grid_remove()

        i = 0
        for descriptions in self.pokemon_data.pokemon_abilities_description_label:
            self.pokemon_data.pokemon_abilities_description_label[i].grid_remove()
            
        self.pokemon_data.pokemon_abilities_var.clear()
        self.pokemon_data.pokemon_abilities_description_var.clear()
        self.pokemon_data.pokemon_abilities_label.clear()
        self.pokemon_data.pokemon_abilities_description_label.clear()
                
        for abilities in list(pokemon.abilities.keys()):
            self.pokemon_data.pokemon_abilities_var.append(abilities)

        for abilities in list(pokemon.abilities.keys()):
            poke_ability = self.poke_info.get(ability=pokemon.abilities[abilities][16:-1])
            self.pokemon_data.pokemon_abilities_description_var.append(poke_ability.description)

        i = 0
        for abilities in self.pokemon_data.pokemon_abilities_var:
            print(self.pokemon_data.pokemon_abilities_var[i])
            label = Label(self.pokemon_frames.abilities_frame, text=self.pokemon_data.pokemon_abilities_var[i])

            self.pokemon_data.pokemon_abilities_label.append(label)
            label.grid(column=0, row=i+1)
            print(self.pokemon_data.pokemon_abilities_description_var[i])
            label = Label(self.pokemon_frames.abilities_frame, text=self.pokemon_data.pokemon_abilities_description_var[i])
            label.grid(column=1, row=i+1)
            self.pokemon_data.pokemon_abilities_description_label.append(label)
            i = i + 1

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

        i = 0
        for evolutions in pokemon.evolutions:
            pokemon_evolution = poke_info.get(pokemon=pokemon.evolutions[evolutions][16:-1])
            print(pokemon_evolution.sprites[list(pokemon_evolution.sprites.keys())[0]])
            evolution_sprite_info = poke_info.get(sprite=pokemon_evolution.sprites[list(pokemon_evolution.sprites.keys())[0]][15:-1])
            evolution_sprite = poke_info.get_sprite(evolution_sprite_info.image)
            evolution_sprite.thumbnail((80,80))
            evolution_sprite = ImageTk.PhotoImage(evolution_sprite)
            
            self.pokemon_data.pokemon_evolution_display_image.append(evolution_sprite)

            poke_sprite_display = Canvas(self.pokemon_frames.evolution_frame, width=80, height=80, bg='white')
            poke_sprite_display.create_image(40, 40, image=self.pokemon_data.pokemon_evolution_display_image[-1])
            poke_sprite_display.image = self.pokemon_data.pokemon_evolution_display_image[-1]
            self.pokemon_data.pokemon_evolution_sprite.append(poke_sprite_display)
            poke_sprite_display.grid(column=i, row=1)

            label = Label(self.pokemon_frames.evolution_frame, text=pokemon_evolution.name)
            self.pokemon_data.pokemon_evolution_name.append(label)
            label.grid(column=i, row=2)

            i = i+1
            
        self.pokemon_data.pokemon_egg_cycles_var.set(str(pokemon.egg_cycles))
        self.pokemon_data.pokemon_growth_rate_var.set(str(pokemon.growth_rate))
        
        if len(pokemon.egg_groups) == 1:
            self.pokemon_data.pokemon_egg_group_var.set(list(pokemon.egg_groups)[0])
        else:
            self.pokemon_data.pokemon_egg_group_var.set(list(pokemon.egg_groups)[0] + " and " + list(pokemon.egg_groups)[1])

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
    poke_info = get_pokemon_information.pokemon_information()
    menubar = Menu(root)
    menubar.add_command(label='Build Cache', command=poke_info.buildCache)
    root.config(menu=menubar)
    img = PhotoImage(file='pokeball.png')
    root.tk.call('wm', 'iconphoto', root._w, img)
    app = Application(root)
    app.master.title('Pokedex')
    app.mainloop()
