print("%4d" % int(input('Введіть перше число ')))

print("{0:4d}".format(int(input('Введіть друге число '))))

f = float(input('Введіть третє число '))
print("{0:9f}".format(f))

f_2 = float(input('Введіть четверте число '))
print("{0:6.3f}".format(f_2))

string = str(input("Введіть п'яте число "))
false = False if len(string) != 3 or string == "False" else True
print(false)

