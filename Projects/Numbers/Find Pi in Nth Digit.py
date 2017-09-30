import math
import sys

input_length = input("Wie viele Nachkommastellen von Pi wollen Sie berechnen?: ")
n = input_length
    

def calculate_Pi(n):

    if(n > 10):
        print("Dieses Programm kann leider nur 10 Nachkommastellen berechnen")
        sys.exit()

    pi = math.pi
    pi_rounded = round(pi, n)
    return pi_rounded

    
        


print(calculate_Pi(n))