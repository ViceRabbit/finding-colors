import numpy as np 
import json 

with open('/workspace/finding-colors/robloxBrickColors.json', 'r') as colorJson:
    brickColorDict = json.load(colorJson) # establishing dictionary of brick colors

allColorsArray = np.array(list(brickColorDict.values()))
desiredColor = np.array(input("Type in the RGB Value of your color; seperated in commas - ").split(", "), dtype=np.int32) # int32 in order to convert str to integers for np array

differences = np.sum(np.abs(allColorsArray-desiredColor), axis=1) # sums up all differences :D (abs is used to prevent negatives & axis 1 to sum up horizontally)
closestRGB = list(allColorsArray[np.where(differences == np.min(differences))][0]) # indexes the color; where.() returns the index of the the least difference. [0] is used to flatten as its [[x]]

for x in brickColorDict: # finding name of rgb brickcolor
    if brickColorDict[x] == closestRGB:
        brickName = x
        break 

print(f"The closest RGB value for {desiredColor} is {brickName}; {closestRGB}.")





