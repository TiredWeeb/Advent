File = open("Input.txt","r")
TotalScore = 0
#Points given for what you throw
PointsDictionary = {"X" : 1,  "Y" : 2,  "Z" : 3}
OpponentChoice = "A"

#Loops through every round(line) in the input file
for Thing in File:
  TotalScore += PointsDictionary[Thing[2]]

  #Shifts letters over 23 characters to make the letters the same
  Char = chr(ord(Thing[0]) + 23)

  #Checks the result of the round if they tied it adds 3 points, 6 if you won, and 0 if you lost
  if Char == Thing[2]:
    TotalScore +=3
  elif (Char == "X" and Thing[2] == "Y") or (Char == "Y" and Thing[2] == "Z") or (Char == "Z" and Thing[2] == "X"):
    TotalScore+=6

print(TotalScore)