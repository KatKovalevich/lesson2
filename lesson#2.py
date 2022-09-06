# задача 1
my_li = [1, 2, 3, 4, 5, 'вышел', 'зайчик', 'погулять']
for i in range(0, len(my_li)):
    print(f"Тип переменной: {type(my_li[i])}")

# задача 4
ph = input("Введите текст:").split()
print(ph)
for i, el in enumerate(ph, 1):
    if len(el) > 10:
        el = el[:10]
        print(f'{i}. {el}')
    else:
        print(f'{i}. {el}')

# задача 2
a = (input('Введите элементы списка:')).split()
a[:-1:2], a[1::2] = a[1::2], a[:-1:2]
print(a)

# задача 3
nm = int(input('Введите номер месяца от 1 до 12:'))
lm = ['зима', 'весна', 'лето', 'осень']
if nm >= 1 and nm < 3:
    print(lm[0])
elif nm >= 3 and nm < 6:
    print(lm[1])
elif nm >= 6 and nm < 9:
    print(lm[2])
elif nm >= 9 and nm < 12:
    print(lm[3])

seas = {'зима': [12, 1, 2], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}
mon = int(input('Введите номер месяца:'))
for el in seas:
    if mon in seas[el]:
        print(el)

# задача 5
ml = [7, 5, 3, 3, 2]
r = int(input('Введите число:'))
if r > 0:
    ml.append(r)
    ml.sort(reverse=True)
    print(ml)














