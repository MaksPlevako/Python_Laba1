hour = float(input('Введіть години (від 0 до 11) = '))
minute = float(input('Введіть хвилини (від 0 до 59) = '))
second = float(input('Введіть секунди (від 0 до 59) = '))

gr = float(360/(12*60*60))
second = float((hour*3600)+(minute*60)+second)
corner = float(second*gr)

print('%.2f' % corner,' градусів')


