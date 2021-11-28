import UnityPy
import random
from PyQt5.QtWidgets import QTextEdit
import os
from pathlib import Path

#PathIDs inside Unity
#DO NOT CHANGE UNLESS GAME IS UPDATED
Trainer_Table = 676024375065692598
modPath = "romfs/StreamingAssets/AssetAssistant/Dpr"
pathList = [Trainer_Table]

#Level Increase
LevelIncrease = 1.5

def getAbilityList():
    
    filepath = "Resources//ability.txt"
    with open(filepath, "r") as f:
        return f.read().splitlines()
    
def getMoveList():
    
    filepath = "Resources//moves.txt"
    with open(filepath, "r") as f:
        return f.read().splitlines()

def RandomizeTrainers(text):
    # make sure masterdatas is in same folder
    cwd = os.getcwd()
    
    abilityList = getAbilityList()
    moveList = getMoveList()
    
    if os.path.exists(modPath) == True:
        if os.path.isfile(modPath + '/masterdatas') == True:
            os.chdir(modPath)


    src = "masterdatas"

    env = UnityPy.load(src)
    extract_dir = "Walker"
    text.append("Trainers Loaded.")
    
    
    for obj in env.objects:
        if obj.path_id in pathList:
            tree = obj.read_typetree()

            #TrainerPoke
            if tree['m_Name'] == "TrainerTable":
                for dic in tree['TrainerPoke']:
                    for pokeNum in range(1, 7):
                        # print(dic["P"f"{pokeNum}Level"])
                        level = dic["P"f"{pokeNum}Level"]
                        if level > 0:
                            #Increases level by 50% with a cap at level 100
                            dic["P"f"{pokeNum}Level"] = int(dic["P"f"{pokeNum}Level"] * LevelIncrease)
                            if dic["P"f"{pokeNum}Level"] > 100:
                                dic["P"f"{pokeNum}Level"] = 100
                            newPokemon = random.randint(1,493)
                            dic["P"f"{pokeNum}MonsNo"] = newPokemon
                            
                            ##Ability Selection
                            dic["P"f"{pokeNum}Level"] = int(random.choice(abilityList[newPokemon-1][1:-1]))
                            
                            possibleMoves = []
                            monMoveList = moveList[newPokemon-1].split(",")[1:-1]
                            for i in range(int(len(monMoveList[:-1])/2)):
                                if int(monMoveList[i*2]) < dic["P"f"{pokeNum}Level"]:
                                    possibleMoves.append(int(monMoveList[i*2 + 1]))
                                    
                            # print(possibleMoves)
                            ##Moves 1 through 4
                            amountOfMoves = min(4, len(possibleMoves))
                            for moveNum in range(1, amountOfMoves + 1):
                                dic["P"f"{pokeNum}Waza"f"{moveNum}"] = possibleMoves[-moveNum]
                                
                            
                            # Set all IVs to 31 for maximum difficulty :P
                            dic["P"f"{pokeNum}TalentHp"] = 31
                            dic["P"f"{pokeNum}TalentAtk"] = 31
                            dic["P"f"{pokeNum}TalentDef"] = 31
                            dic["P"f"{pokeNum}TalentSpAtk"] = 31
                            dic["P"f"{pokeNum}TalentSpDef"] = 31
                            dic["P"f"{pokeNum}TalentAgi"] = 31
                               
                obj.save_typetree(tree)
                
            else:
                print("Error use different path_id")
                
           
            
                    
    text.append("Trainers Randomized.")                
    # saving an edited file
    # apply modifications to the objects
    # don't forget to use data.save()
        # ...
        # 
        # 
    #This output is compressed, thanks to Copycat#8110
    if cwd == os.getcwd():
        Path(modPath).mkdir(parents=True, exist_ok=True)
        os.chdir(modPath)
        
    with open("masterdatas", "wb") as f:
        f.write(env.file.save(packer = (64,2)))
    text.append("Trainers Saved.")
    
    os.chdir(cwd)
