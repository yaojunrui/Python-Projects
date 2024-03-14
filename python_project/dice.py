import random

max = 6
min = 1

roll = True

while roll:
    print("开始投骰子\n")
    print("点数是: ")
    
    print(random.randint(min, max))
    
    if (input("继续投?(y/n): ") == "y") :
        roll = True
    else:
        roll = False
        
