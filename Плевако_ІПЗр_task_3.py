import math

a = int(input('a = '));
b = int(input('b = '));
x = float((a+b)/2);
s = float((math.sqrt(a*b)));
print ('Cереднє арифметичне','%10.2f'% x);
print ('Cереднє геометричне','%10.3f'% s);
