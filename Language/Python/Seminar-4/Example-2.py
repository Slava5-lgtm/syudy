# Example-2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:

# 1) с помощью математических формул нахождения корней квадратного уравнения
#     2) с помощью дополнительных библиотек Python(scipy)

import math

a = 3
b = 9
c = 4 

D = b ** 2 - 4 * a * c

x1 = (b + (math.sqrt(D))) / 2 * a

x2 = (b - (math.sqrt(D))) / 2 * a

print(x1)  
print(x2)





