import sys

n = int(input("Enter a value: "))
nInitial = str(n)
count = 0


def isEven(n):      #is number even?
    if n%2 == 0:
        return True

    elif n%2 != 0:
        return False

def isOdd(n):       #is number odd?
    if n%2 == 0:
        return False

    elif n%2 != 0:
        return True


while (n != 1):

    

    if (isEven(n) == True and isOdd(n) == False):
        n = n / 2
        count = count + 1
        
    
    elif (isOdd(n) == True and isEven(n) == False):
        n = n * 3 + 1
        count = count + 1
        

    print (count, n)

print ("Die Zahl %s brauch %s Iterationen um auf 1 zu kommen" %(nInitial, count))

sys.exit()
