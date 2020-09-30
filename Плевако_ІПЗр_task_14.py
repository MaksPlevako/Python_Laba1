import math

print ('Введіть координати першої точки (через пробіл) ', end = '')
a1, a2 = map(float, input().split())
print ('Введіть координати другої точки (через пробіл) ', end = '')
b1, b2 = map(float, input().split())
print ('Введіть координати третьої точки (через пробіл) ', end = '')
c1, c2 = map(float, input().split())

AB = float((math.sqrt((a2-a1)**2+(b2-b1)**2)))
BC = float((math.sqrt((b2-b1)**2+(c2-c1)**2)))
AC = float((math.sqrt((a2-a1)**2+(c2-c1)**2)))
P = AB + BC + AC
p = P/2
S = (math.sqrt(p*(p - AB)*(p - BC)*(p - AC)))

print( 'Периметр трикутника дорівнює','%.2f' %  P)
print('Площа трикутника дорівнює','%.2f' %  S)

