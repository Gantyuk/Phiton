import math
 
x = float(input('x = '))
a = float(input('a = '))
e = float(input('e = '))
suma = 0
k = 1
precision = math.pow(math.log(a + x), 2 * k) / (math.pow(2, k) + math.factorial(k))
while math.fabs(precision) > e:
    precision = math.pow(math.log(a + x), 2 * k) / (math.pow(2, k) + math.factorial(k))
    suma +=precision 
    k = k + 1
	
print("Сума=" + str(suma))
print("Кількість врахованих доданків:" + str(k))
