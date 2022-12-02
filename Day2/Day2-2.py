File = open("Input.txt","r")
TotalScore = 0
#Points given for what you throw
PointsDictionary = {"X" : 1,  "Y" : 2,  "Z" : 3}
WinOptions = {"X" : "Y", "Y" : "Z", "Z" : "X"}
LoseOptions = {"X" : "Z", "Y" : "X", "Z" : "Y"}

#Loops through every round(line) in the input file
for Thing in File:
  Char = chr(ord(Thing[0]) + 23)

  if Thing[2] == "X": #Lose
      TotalScore += PointsDictionary[LoseOptions[Char]]
  elif Thing [2] == "Y": #Draw
      TotalScore += 3
      TotalScore += PointsDictionary[Char]
  elif Thing [2] == "Z": #Win
      TotalScore +=6
      TotalScore += PointsDictionary[WinOptions[Char]]

print(TotalScore)