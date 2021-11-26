import UnityPy
import random

#PathIDs inside Unity
#DO NOT CHANGE UNLESS GAME IS UPDATED
Trainer_Table = 676024375065692598

pathList = [Trainer_Table]

# make sure masterdatas is in same folder
src = "masterdatas"

env = UnityPy.load(src)
extract_dir = "Walker"

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
                        dic["P"f"{pokeNum}Level"] = int(dic["P"f"{pokeNum}Level"] * 1.5)
                        # if dic["P"f"{pokeNum}Level"] > 100:
                        #     dic["P"f"{pokeNum}Level"] = 100
                        newPokemon = random.randint(1,493)
                        dic["P"f"{pokeNum}MonsNo"] = newPokemon
                        ##Moves 1 through 4
                        dic["P"f"{pokeNum}Waza1"] = 52
                        dic["P"f"{pokeNum}Waza2"] = 52
                        dic["P"f"{pokeNum}Waza3"] = 52
                        dic["P"f"{pokeNum}Waza4"] = 52
                        #Set all IVs to 31 for maximum difficulty :P
                        dic["P"f"{pokeNum}TalentHp"] = 31
                        dic["P"f"{pokeNum}TalentAtk"] = 31
                        dic["P"f"{pokeNum}TalentDef"] = 31
                        dic["P"f"{pokeNum}TalentSpAtk"] = 31
                        dic["P"f"{pokeNum}TalentSpDef"] = 31
                        dic["P"f"{pokeNum}TalentAgi"] = 31

            obj.save_typetree(tree)
            
        else:
            print("Error use different path_id")
                
                
# saving an edited file
# apply modifications to the objects
# don't forget to use data.save()
    # ...
    # 
    # 
#This output is compressed, thanks to Copycat#8110
with open("randomTrainers", "wb") as f:
    f.write(env.file.save(packer = (64,2)))
