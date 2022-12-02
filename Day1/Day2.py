File = open("Input.txt","r")

Table = []
Count = 0

for Number in File:
    if Number != "\n":
        if len(Table) > Count:
            Table[Count] += int(Number)
        else:
            Table.append(int(Number))
    else:
        Count+=1

CalorieCount = 0

Table.sort(reverse=True)

CalorieCount = Table[0] + Table[1] + Table[2]

print(CalorieCount)