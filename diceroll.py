import random
import re

repeat = True
answer = "random"
num = 1
dice = 2
addDigit = 0
previousResult = 0
secondDice = 2
secondNum = 1
previousResult_2 = 0

# random.randint(1,20)
#repeat = "#help" in input()
#help
#command to roll dice:
# /r [(n)dice]
#to add numbers into dice roll:
# /r [(n)dice] + (n)
#to add dice into dice roll:
# /r [(n)dice] + [(n)dice]
repeat = input("Type '#help' to display command list. Otherwise type anything else. \n")

if repeat == "#help":
    print("command to roll dice: \n/r [(n)dice] \n\nto add numbers into dice roll: \n/r [(n)dice] + (n)\n\nto add dice into dice roll:\n/r [(n)dice] + [(n)dice]")
    repeat = input("Type '#help' to display command list. Otherwise type anything else. \n")
    
else:
    while repeat:
        answer = input("Roll a dice. \n")
    
        if "/r" in answer:
            
            
            if "+" in answer:
                one_half = answer.split("+")[0]
                dice = int(one_half.rsplit("d", -1)[1])
                
                second_half = answer.split("+")[1]
                second_half = second_half.replace(" ", "")
                
                if second_half.isdigit():
                    addDigit = int(second_half)
                    
                else:
                    addDigit = 0
                    answer = one_half
                    secondDice = int(second_half.rsplit("d", 1)[-1])
                    
                    secondNum = re.findall(r"(\d+)d", second_half)
                    
                    for i in range(0, len(secondNum)): 
                        secondNum[i] = int(secondNum[i])
                        
                        secondNum = [str(n) for n in secondNum]
                        secondNum = "".join(secondNum)
                        secondNum = int(secondNum)
                    
                    if secondDice % 2 == 0:
                
                        if not secondNum:
                            secondNum = 1
                            
                        for i in range(0, secondNum):
                            result = random.randint(1, secondDice)
                            previousResult_2 += result
                            
                        addDigit = previousResult_2
                
            else:
                dice = int(answer.rsplit("d", 1)[-1])
                

            num = re.findall(r"(\d+)d", answer)
            previousResult = 0
            
            for i in range(0, len(num)): 
                num[i] = int(num[i])
                
                num = [str(n) for n in num]
                num = "".join(num)
                num = int(num)
                
#                 print(num)
            
            if dice % 2 == 0:
#                 print("Number: ", num)
#                 print("Dice: ", dice)
                
                if not num:
                    num = 1
                    
                for i in range(0, num):
                    result = random.randint(1, dice)
                    print("Rolling", i + 1,"d", dice, ": " ,result)
                    previousResult += result
                    
                
                previousResult += addDigit
                print("Adding: ", addDigit)
                print("Total: ", previousResult)
                
            else:
                print("Command not found. Roll again? Y/N")
                repeat = "Y" in input()
    
        else:
            print("Command not found. Roll again? Y/N")
            repeat = "Y" in input()