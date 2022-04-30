#Thomas Dreitlein
#Course Project: Comfy Deviation

import math
import statistics

inputA = int(input("Enter a Room Temperature Value:"))
inputB = int(input("Enter a 2nd Room Temperature Value:"))
inputC = int(input("Enter a 3rd Room Temperature Value:"))
inputD = int(input("Enter a 4th Room Temperature Value:"))
inputE = int(input("Enter a 5th Room Temperature Value:"))
inputF = int(input("Enter a 6th Room Temperature Value:"))
inputG = int(input("Enter a 7th Room Temperature Value:"))
inputH = int(input("Enter a 8th Room Temperature Value:"))
inputJ = int(input("Enter a 9th Room Temperature Value:"))
inputK = int(input("Enter a 10th Room Temperature Value:"))



average = ((inputA + inputB + inputC + inputD + inputE + inputF + inputG + inputH + inputJ + inputK) / 10)


devA = math.sqrt(((inputA - average)**2)/(10-1))
devB = math.sqrt(((inputB - average)**2)/(10-1))
devC = math.sqrt(((inputC - average)**2)/(10-1))
devD = math.sqrt(((inputD - average)**2)/(10-1))
devE = math.sqrt(((inputE - average)**2)/(10-1))
devF = math.sqrt(((inputF - average)**2)/(10-1))
devG = math.sqrt(((inputG - average)**2)/(10-1))
devH = math.sqrt(((inputH - average)**2)/(10-1))
devJ = math.sqrt(((inputJ - average)**2)/(10-1))
devK = math.sqrt(((inputK - average)**2)/(10-1))

#inputA, inputB, inputC, inputD, inputE, inputF, inputG, inputH, inputJ, inputK

if devA <= 1.0 and devB <= 1.0 and devC <= 1.0 and devD <= 1.0 and devE <= 1.0 and devF <= 1.0 and devG <= 1.0 and devH <= 1.0 and devJ <= 1.0 and devK <= 1.0:
    print(inputA, inputB, inputC, inputD, inputE, inputF, inputG, inputH, inputJ, inputK, "Comfy")   
else:
    print(inputA, inputB, inputC, inputD, inputE, inputF, inputG, inputH, inputJ, inputK, "Not Comfy")   


