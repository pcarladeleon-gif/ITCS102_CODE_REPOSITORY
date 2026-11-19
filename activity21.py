sum = 0 

continous = True 

while continous == True:
    x = int(input(" please enter a number--->  "))

    if x == 0:
        print("loop terminated")
        print("the current amount is", sum)
        break

    else:
        print("continues loop")
        print(" your total number is",sum)
        sum += x
        continue


