count_passengers = int(input("Кількість пасажирів : "))
count_cameras = int(input("Кількість камер схову : "))
l = []
s = 0
ansver = []
i = 0

while s < count_passengers:
    l.append(0)
    s += 1
print ("Вводіте пасажирів : ")  
while i < count_passengers:
    name, begin, end = input().split(' ')
    begin_hour, begin_min = begin.split(':')
    end_hour, end_min = end.split(':')
    begin = int(begin_hour) * 60 + int(begin_min)
    end = int(end_hour) * 60 + int(end_min)
    j = 0
    while j < count_cameras:
        if l[j] <= begin:
            l[j] = end
            ansver.append([name, j+1])
            break
        j += 1
    i += 1
    
for name, i in ansver:
    print (name, i)
