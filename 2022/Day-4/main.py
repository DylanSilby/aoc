file = open("2022\\Day-4\\input.txt", "r+")
Lines = file.readlines()
file.close()
pairList = []
containsOther = 0
#part 1
for i in Lines:
  Pair = i.split(",")
  start1, start2 = int(Pair[0].split("-")[0]), int(Pair[1].split("-")[0])
  end1, end2 = int(Pair[0].split("-")[1]), int(Pair[1].split("-")[1])
  if (start1 <= start2 and end1 >= end2):
    containsOther += 1
  elif (start2 <= start1 and end2 >= end1):
    containsOther += 1
print(containsOther)
containsOther = 0
#part 2
for i in Lines:
  Pair = i.split(",")
  start1, start2 = int(Pair[0].split("-")[0]), int(Pair[1].split("-")[0])
  end1, end2 = int(Pair[0].split("-")[1]), int(Pair[1].split("-")[1])
  range1 = range(start1, end1 + 1)
  range2 = range(start2, end2 + 1)
  if (len(set(range1) & set(range2)) > 0):
    containsOther += 1
print(containsOther)
#these sure are something
