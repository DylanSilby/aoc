file = open("2022\\Day-1\\Input.txt", "r+")
fileLines = file.readlines()
elf = 1
highestScore = 0
highestElf = 1
score = 0
elfs = [];
#working version but I didn't like the use of the while loop and the try to remove the error
# while fileLines:
#   # use realine() to read next line
#   fileLines = file.readline()
#   if(fileLines != "\n"):
#     try: 
#       score += int(fileLines)
#     except:
#       print(fileLines)
#   if(fileLines == "\n"):
#     elf+=1
#     if(score > highestScore):
#       highestScore = score
#       highestElf = elf
#     elfs.append(score)
#     score = 0

for i in fileLines:
    if(i != "\n"):
        score+= int(i)
    if(i == "\n"):
        elf+=1
        if(score > highestScore):
            highestScore = score
            highestElf = elf
        elfs.append(score)
        score = 0
print(highestScore, highestElf)
elfs = sorted(elfs, reverse=True)
print(elfs[0]+elfs[1]+elfs[2])
file.close()