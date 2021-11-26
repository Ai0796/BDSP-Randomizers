import UnityPy
import random


#PathIDs inside Unity
#DO NOT CHANGE UNLESS GAME IS UPDATED
evolveTable = 5139195221601552760

pathList = [evolveTable]
# make sure the file personal_masterdatas is in this folder
# personal_masterdatas is inside Pml
src = "personal_masterdatas"

env = UnityPy.load(src)

##One to one
r = random.sample(range(1,561), 560)

i = 0

for obj in env.objects:
    
    if obj.path_id in pathList:
        tree = obj.read_typetree()
        
        if tree['m_Name'] == "EvolveTable":
            for monID in tree['Evolve']:
                monID["ar"] = [4, 0, r[i], 0, 1] 
                i += 1
            #Saves the object tree
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
with open("randomEvolutions", "wb") as f:
    f.write(env.file.save(packer = (64,2)))
