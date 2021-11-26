#py -m pip install UnityPy
import UnityPy
import random
from PyQt5.QtWidgets import *

#PathIDs inside Unity
#DO NOT CHANGE UNLESS GAME IS UPDATED
diamondEncount = 361824127573837173
pearlEncount = -9035030829162387677

pathList = [diamondEncount, pearlEncount]
lengendaries = [144,145,146,150,151,243,244,245,249,250,251,377,378,379,380,381,382,383,384,385,386,480,481,482,483,484,485,486,487,488,491]

# make sure the file gamesettings is in this folder
# gamesettings is in Dpr/scriptableassets
def RandomizeEncounters(text):
    src = "gamesettings"
    
    env = UnityPy.load(src)  
    text.append("Gamesettings Loaded.")
    Encount(1, env, text)

    # saving an edited file
    # apply modifications to the objects
    # don't forget to use data.save()
        # ...
        # 
        # 
    #This output is uncompressed, make sure to compress using LZ4 in UABEA
    with open("gamesettings", "wb") as f:
        f.write(env.file.save(packer = (64,2)))
    text.append("Encounters Saved.")
 
#Have to move this outside of the function because im calling it from another file -- Sangawku
# Legends = 1 will keep legendariy encounters legendary, i.e. Palkia will become Mewtwo or something, not wurmple
def Encount(legend, env, text):
    text.append("Randomizing Pokemon.")
    for obj in env.objects:
        
        if obj.path_id in pathList:
            tree = obj.read_typetree()
            
            ##Two encounter tables are named FieldEncountTable_d (diamond) and FieldEncountTable_p (pearl)
            for area in tree['table']:
                for key in area.keys():
                    if type(area[key]) != int:
                        if type(area[key][0]) == dict:
                            for mon in area[key]:
                                if mon['monsNo'] != 0:
                                    if legend == 1:
                                        for legsNo in lengendaries:
                                            if mon['monsNo'] == legsNo:
                                                mon['monsNo'] = random.choice(lengendaries)
                                    else:
                                        mon['monsNo'] = random.randint(1,493)
            #Saves the object tree
            obj.save_typetree(tree)
            text.append("Randomzing Done.")
