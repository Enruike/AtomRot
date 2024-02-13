import os
import sys
import math

argumentList = sys.argv[1:]

#for number in range(1, 4):
    #argumentList[number] = float(argumentList[number])
    #print(argumentList[number])
if argumentList:
    print
else:
    print("-----------------------------------------------------------------------")
    print(" ~ Valid input format should be: FileName.input.txt Alpha Beta Gamma ~ ")
    print("-----------------------------------------------------------------------")
    sys.exit()

alpha = float(argumentList[1])
beta = float(argumentList[2])
gamma = float(argumentList[3])

fileList = []

if argumentList[0] == 'all':
    print("All files will be rotated!")
    for file in os.listdir('.'):
        if file.endswith(".out.txt") or file.endswith(".input.txt"):
            fileList.append(file)
    
    if fileList:
        print("Found files:")
        for files in fileList:
            print(files)
        print("")
    else:
        print("No files were found!")
        sys.exit()

else:
    print(argumentList[0], "file will be rotated")
    fileList = [argumentList[0]]

print("Rotational Angles are Alpha:", alpha,", Beta:", beta,", Gamma: ", gamma)
alpha = math.radians(alpha)
beta = math.radians(beta)
gamma = math.radians(gamma)

print("--------------------------------")
print(" ~ ~ Starting Atom Rotation ~ ~ ")
print("--------------------------------")

for files in fileList:
    file = open(files, 'r')
    lines = file.readlines()

    print("======>", files)

    f = open("rot_" + files, 'w')
    f.write(str(lines[0].split()[0]) + '\n')

    for line in lines[2:]:
        dataLine = line.split()
        f.write("\n" + f"{dataLine[0] : <5}")
        x = float(dataLine[1])
        y = float(dataLine[2])
        z = float(dataLine[3])

        x_rot = x * math.cos(alpha) * math.cos(beta) + y * (math.cos(alpha) * math.sin(beta) * math.sin(gamma) - math.sin(alpha) * math.cos(gamma)) + z *(math.cos(alpha) * math.sin(beta) * math.cos(gamma) + math.sin(alpha) * math.sin(gamma))
        y_rot = x * math.sin(alpha) * math.cos(beta) + y * (math.sin(alpha) * math.sin(beta) * math.sin(gamma) + math.cos(alpha) * math.cos(gamma)) + z *(math.sin(alpha) * math.sin(beta) * math.sin(gamma) - math.cos(alpha) * math.sin(gamma))
        z_rot = -x * math.sin(beta) + y * math.cos(beta) * math.sin(gamma) + z * math.cos(beta) * math.cos(gamma)
        
        x_rot = round(x_rot, 6)
        y_rot = round(y_rot, 6)
        z_rot = round(z_rot, 6)

        f.write(f"{x_rot : ^20}{y_rot : ^20}{z_rot : ^20}")
    
    f.close()
    
print("~ Done ~")