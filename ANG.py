#!/usr/bin/python3

import random
input = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
input2 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
y = random.randint(0, 5)

output = []
length = 48

for z in range(0, length):
    m = random.randint(0, 1)
    if m == 0:
        source = input
        maxcharvalue = 23
    else:
        source = input2
        maxcharvalue = 9
    x = random.randint(0, maxcharvalue)
    z += 1
    output.append(source[x])
    
print("".join(output))