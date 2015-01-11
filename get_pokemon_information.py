import pykemon.request as poke_request
from pykemon.request import CLASSES
from PIL import Image

import requests
import os
import simplejson
import glob

class pokemon_information:
    def get(self, **choice):
        name = choice[list(choice.keys())[0]]
        resource_type = list(choice.keys())[0]
        if not os.path.exists("cache/"+resource_type):
            print("Creating Directory for reasource")
            os.mkdir("cache/"+resource_type)

        if glob.glob("cache/"+resource_type+"/"+name+" -*.json"):
            print("Getting resource from file")
            data_file = open(glob.glob("cache/"+resource_type+"/"+name+" -*.json")[0])
            data = self.get_data_as_data(data_file.read(), resource_type)
            data_file.close()
            return data
        
        if glob.glob("cache/"+resource_type+"/*- "+name+".json"):
            print("Getting resource from file")
            data_file = open(glob.glob("cache/"+resource_type+"/*- "+name+".json")[0])
            data = self.get_data_as_data(data_file.read(), resource_type)
            data_file.close()
            return data
        
        print("Retreiving resource from internet")
        data = self.get_data_json(choice)
        resource = self.get_data_as_data(data,resource_type)
        data_file = open("cache/"+resource_type+"/"+str(resource.id)+" - "+resource.name+".json", 'w+')
        data_file.write(data)
        data_file.close()
        return resource


    def get_data_json(self,choice):
        uri, nchoice = poke_request._compose(choice)
        data = requests.get(uri)
        return data.text

    def get_data_as_data(self,data_file,resource_type):
        data =  simplejson.loads(data_file)
        resource = CLASSES[resource_type]
        return resource(data)

    def get_sprite(self, uri):
        print("Getting sprite")
        if not os.path.exists('cache/media'):
            os.mkdir('cache/media')
            os.mkdir('cache/media/image')
        if glob.glob('cache/media/image/'+uri[11:]):
            print("Getting sprite from file")
            image = Image.open('cache/media/image/'+uri[11:])
            return image
        print("Retreiving Sprite from the internet")
        sprite_file = open('cache/media/image/temp.png', 'wb')
        sprite = requests.get('http://pokeapi.co/'+uri).content
        sprite_file.write(sprite)
        sprite_file.close()

        #make sure all sprites are the same size
        img = Image.open('cache/media/image/temp.png')
        size = 120, 120
        img.thumbnail(size)
        img.save('cache/media/image/'+uri[11:], "PNG")
        img.close()
        
        image = Image.open('cache/media/image/'+uri[11:])
        return image
