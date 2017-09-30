import math
import sys

input_length = input("Wie viele Nachkommastellen von e wollen Sie berechnen?: ")
n = input_length
    

def calculate_e(n):

    if(n > 10):
        print("Dieses Programm kann leider nur 10 Nachkommastellen berechnen")
        sys.exit()

    e = math.e
    e_rounded = round(e, n)
    return e_rounded

    
        


print("e = %s") %(calculate_e(n))