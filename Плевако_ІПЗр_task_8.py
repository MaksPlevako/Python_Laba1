print("Введіть день року '1 <= number day <= 365'", end ='')
day = int(input())

if day <= 0:
        print("Невірно введені дані")
elif day > 365:
        print("Невірно введені дані")
elif day % 7 == 0:
        print("Неділя")
elif day % 7 == 1:
        print("Понеділок")
elif day % 7 == 2:
        print("Вівторок")
elif day % 7 == 3:
        print("Середа")
elif day % 7 == 4:
        print("Черверг")
elif day % 7 == 5:
        print("П'ятниця")
elif day % 7 == 6:
        print("Субота")
else:
        print("Помилка")

