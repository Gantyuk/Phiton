from random import randrange as rnd, choice

def scalar_product(vector1,vector2,count1):
    suma=0
    for i in range(count1):
         suma+=vector1[i]*vector2[i]
    return suma

count = int(input('n = '))
matrix = []

for r in range(count):
    matrix.append([])
    for c in range(count):
        matrix[r].append(rnd(10,100))
print("X:")
for r in range(count):
    print(matrix[r])

matrixY= []
for r in range(count):
    matrixY.append([])
    for c in range(count):
        matrixY[r].append(scalar_product(matrix[r],matrix[c],count))
        
print("Y:")     
for r in range(count):
    print(matrixY[r])
