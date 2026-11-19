size = int(input("Enter number --> "))

for x in range (size):
    p = 1
    for y in range (x, size):
        print(" ", end=" ")
    for y in range (x):
        print(p, end= " ")
        p+=1
    for z in range (x+1):
        print(p, end=" ")
        p-=1
    print()