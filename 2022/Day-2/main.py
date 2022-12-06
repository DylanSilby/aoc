mf = open("2022\\Day-2\\input.txt", "r+")

lines = mf.readlines()
score = 0
scoreLookup = {
  "X": 1,
  "Y": 2,
  "Z": 3,
  "A": 1,
  "B": 2,
  "C": 3
}
# part 1
for i in lines:
  if(((i[2] == "X") and (i[0] == "C"))or((i[2] == "Y") and (i[0] == "A"))or((i[2] == "Z") and (i[0] == "B"))):
    score +=6
    score+= scoreLookup.get(i[2])

  if(((i[2] == "X") and (i[0] == "B"))or((i[2] == "Y") and (i[0] == "C"))or((i[2] == "Z") and (i[0] == "A"))):
    score += scoreLookup.get(i[2])

  if(((i[2] == "X") and (i[0] == "A"))or((i[2] == "Y") and (i[0] == "B"))or((i[2] == "Z") and (i[0] == "C"))):
    score += 3
    score += scoreLookup.get(i[2])
print(score)
score = 0
# part 2
for i in lines:
  if(i[2] == "X"): 
    if(i[0] == "A"):
      score+= scoreLookup.get("Z")
    elif(i[0] == "B"):
      score+= scoreLookup.get("X")
    else:
      score+= scoreLookup.get("Y")
  if(i[2] == "Y"):
    score+=3
    score+= scoreLookup.get(i[0])
  if(i[2] == "Z"):
    score+= 6
    if(i[0] == "A"):
      score+= scoreLookup.get("Y")
    elif(i[0] == "B"):
      score+= scoreLookup.get("Z")
    else:
      score+= scoreLookup.get("X")

print(score)