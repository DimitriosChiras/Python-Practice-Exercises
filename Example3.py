arrayLength = 0
setLength = 0
myArray = []
setA = []
setB = []

for index in range(4):
    line = input()
    if index == 0:
        arrayLength = int(line.split(' ')[0])
        setLength = int(line.split(' ')[1])
    if index == 1:
        for num in line.split(' '):
                myArray.append(int(num))
    if index == 2:
        for num in line.split(' '):
                setA.append(int(num))
    if index == 3:
        for num in line.split(' '):
                setB.append(int(num))

happiness = 0
for num in myArray:
    if num in setA:
        happiness += 1
    elif num in setB:
        happiness -= 1

print(happiness)