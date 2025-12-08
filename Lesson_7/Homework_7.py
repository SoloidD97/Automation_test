# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    multiplier = 1

    while True:
        result = number * multiplier

        if result > 25:
            break

        print(number, "x", multiplier, "=", result)
        multiplier += 1

multiplication_table(3)


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def add_numbers(a, b):
    return a + b

print(add_numbers(3, 5))

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def average(numbers):
    return sum(numbers) / len(numbers)

print(average([1, 2, 3, 4]))

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""

def reverse_string(text):
    return text[::-1]

print(reverse_string("hello"))

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

def longest_word(words):
    longest = ""

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest

print(longest_word(["apple", "banana", "kiwi"]))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):

    for i in range(len(str1)):
        if str1[i:i + len(str2)] == str2:
            return i
    return -1

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
def perimeter(side1, side2, side3, side4):
    return side1 + side2 + side3 + side4

print(perimeter(1, 2, 3, 4))
# task 8
def evening_temperature(before_noon, drop_after_noon, rise_evening):
    after_noon = before_noon - drop_after_noon
    evening = after_noon + rise_evening
    return evening

print(evening_temperature(5, 10, 4))
# task 9
def total_books_cost(first_price):
    second_price = first_price + 2
    third_price = (first_price + second_price) // 2
    return first_price + second_price + third_price

print(total_books_cost(8))
# task 10
def warehouse_goods(sum_12, sum_23, total):
    warehouse2 = sum_12 + sum_23 - total
    warehouse1 = sum_12 - warehouse2
    warehouse3 = sum_23 - warehouse2
    return warehouse1, warehouse2, warehouse3

print(warehouse_goods(250449, 222950, 375291))
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""