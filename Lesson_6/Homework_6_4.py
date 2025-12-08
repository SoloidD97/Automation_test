#Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum_pair = 0

for num in numbers:
    if num % 2 == 0:
        sum_pair += num

print("Сума парних чисел:", sum_pair)