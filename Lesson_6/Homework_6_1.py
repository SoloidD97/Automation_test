#Порахувати кількість унікальних символів в строці.
# Якщо їх більше 10 - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()

text = input("Введіть рядок: ")

unique_chars = set(text)

if len(unique_chars) > 10:
    print(True)
else:
    print(False)
