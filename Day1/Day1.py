File = open("Input.txt","r")

BiggestCount = 0
CalorieCount = 0

for Number in File:
  if Number != "\n":
     CalorieCount += int(Number)
  else:
    if CalorieCount > BiggestCount:
        BiggestCount = CalorieCount
    CalorieCount = 0

print(BiggestCount)



# File = open("Input.txt","r")

# Table = []
# Count = 0

# for Number in File:
#     if Number != "\n":
#         if len(Table) > Count:
#             Table[Count] += int(Number)
#         else:
#             Table.append(int(Number))
#     else:
#         Count+=1

# CalorieCount = 0

# Count = 0
# for Elf in Table:
#     if Elf > CalorieCount:
#         CalorieCount = Elf

#     Count+=1 

# print(CalorieCount)

