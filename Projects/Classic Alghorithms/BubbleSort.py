'''

NEED FIX

'''

import sys

# file = open('Inputdata.txt', 'r')
# line = file.read()
# data = line.split()

data = [184, 100, 27, 102, 1, 25]
template = sorted(data)

try:
    def bubble_sort():
        data.index = 0

        for index, value in enumerate(data):
            index2 = index+1
            if data[index] > data[index2]:
                data[index], data[index2] = data[index2], data[index]

    for n in enumerate(data):
        bubble_sort()
        break

except:
    print("Error")
    sys.exit()

print(data)
sys.exit()
