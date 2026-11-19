column = int(input("enter a number of column --> " ))

for x in range (1, 11 ):
    for y in range(1,column ,1):
        print(x,"x",y,"=",x * y, end= "\t")
    print()