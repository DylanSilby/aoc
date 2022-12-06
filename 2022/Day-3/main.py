file = open("2022\\Day-3\\input.txt", "r+")
Lines = file.readlines()
file.close()
#example lines used in the example on AoC so that I know my code is working before I do the entire file
exampleLines = ["vJrwpWtwJgWrhcsFMMfFFhFp",
"jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
"PmmdzqPrVvPwwTWBwg",
"wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
"ttgJtRGJQctTZtZT",
"CrZsJsPPZsGzwwsLwLmpwMDw"]

sumOfPriorities = 0
#part 1
#iterates through the entire file
for i in Lines:
  #Finds the character that appears in both lists
  elems_in_both_lists = set(i[:len(i)//2]) & set(i[len(i)//2:])
  #Puts this character into a list because sets don't support indexing
  character_from_both_lists = list(dict.fromkeys(elems_in_both_lists))
  #Finds the ascii code and converts into where it is in the alphabet
  if(character_from_both_lists[0].islower()):
    #adds the value to the variable sumOfPriorities if its lowercase
    sumOfPriorities += ord(character_from_both_lists[0])-96
  else:
    #adds the value to the variable sumOfPriorities if it's uppercase
    sumOfPriorities += ord(character_from_both_lists[0])-38
print(sumOfPriorities)

#part 2
sumOfPriorities = 0
for i in range(0,len(Lines)-1,3):
  character_from_three_lists = (set(Lines[i].strip()) & set(Lines[i+1].strip())) & set(Lines[i+2].strip())
  badge_character = list(dict.fromkeys(character_from_three_lists))
  if(badge_character[0].islower()):
    #adds the value to the variable sumOfPriorities if its lowercase
    sumOfPriorities += ord(badge_character[0])-96
  else:
    #adds the value to the variable sumOfPriorities if it's uppercase
    sumOfPriorities += ord(badge_character[0])-38

print(sumOfPriorities)