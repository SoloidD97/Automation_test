#Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
# Створіть об'єкт цього класу, представляючи студента. Потім додайте метод до класу "Студент", який дозволяє змінювати середній бал студента.
# Виведіть інформацію про студента та змініть його середній бал.

class Student:
    def __init__(self, name, lastname, age, average_mark):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.average_mark = average_mark

    def set_mark(self, new_mark):
        self.average_mark = new_mark
        return f"Average mark was changed to {self.average_mark}."

my_student = Student("Dmytro", "S", 30, 6)

print(my_student.name)
print(my_student.lastname)
print(my_student.age)
print(my_student.average_mark)
print(my_student.set_mark(8))
print(my_student.average_mark)