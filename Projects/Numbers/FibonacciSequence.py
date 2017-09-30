import sys



def fib(n):
    i = 1
    j = 0
    try:
        for n in range(1,n + 1):
            i,j = j, i + j

            print(j)
        return j
    except:
        print("Ein Fehler ist aufgetreten")

m = input("Wie oft wollen Sie die Fibonacci Sequenz berechnen?: ")
fib(m)
sys.exit()