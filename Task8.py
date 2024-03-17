"""
Zadanie 1

Имеется текстовый файл. Получить текст, в котором в конце каждой строки из заданного файла есть восклицательный знак.
info.txt

jdasdqwd wqdqwd
dqwd dqwd qd dqwd!
Ewqe eqwe q eq!
Dad das
Dasd das asd as

Sample Output:
dqwd dqwd qd dqwd!
Ewqe eqwe q eq!
"""
file = open("Lesson9_1.txt", "r")
file_data = file.read().rstrip().split("\n")
for i in file_data:
    if "!" in i:
        print(i)
print(file_data)
"""
Zadanie 2
Создать файл input.txt и записать в него 10 чисел через пробел. Считать из него эти числа. 
Затем записать их произведение в файл output.txt.
"""
from functools import reduce  # Функция для сравнения последовательности
from operator import mul  # Функция, перемножающая 2 числа

numbers = input("Введите 10 чисел,через пробел: ")
numbers = numbers.split()
numbers = list(map(int, numbers))

with open(file='input.txt', mode='w') as file_input:
    file_input.write(str(numbers))
file_input.close()

sum_numbers = reduce(mul, numbers)
print(f'Сумма произведения: {sum_numbers}')

with open(file='output.txt', mode='w') as file:
    file.write(str(sum_numbers))
file.close()

"""
Zadanie 3

Список товаров, имеющихся на складе, включает в себя наименование товара, количество единиц товара, цену единицы. 
Вывести список товаров стоимость которых превышает 1 000 000 р.
goods.txt

tv-set 300 5000
cars 700 20000
plane 11 100000
doors 1000 350

Sample Output:
[“plane”, “cars”]
"""
file_goods = open("goods.txt", "w+")
file_goods.write("""tv-set 300 5000
cars 700 20000
plane 11 100000
doors 1000 350""")
file_goods.close()

file_goods = open("goods.txt", "r")
file_2 = file_goods.read().rstrip().split("\n")
x = {}

for value in file_2:
    temp_value = value.split(" ")
    if int(temp_value[1]) * int(temp_value[2]) > 1000000:
        print(temp_value[0])

file_goods.close()

"""

Zadanie 4

Написать программу “Викторина”. У вас есть 2 файла. В первом содержаться 10 вопросов(каждый вопрос в своей строке) 
во втором 10 ответов( каждый ответ как и вопрос в своей строке). 
Вам нужно считывать по 1 вопросу из файла с вопросами и давать на них ответ. Если ответ верный, добавлять к счётчику верных ответов 1 балл. 
В конце программа выводит количество верных ответов на вопросы.
Questions.txt

Столица Великобритании?
Страна производитель Пежо?
…

Answers.txt 

Лондон
Франция
…

Sample Output:
Столица Великобритании?
Страна производитель Пежо?
Верных ответов: 1

Sample Input:
Лондон
Италия
"""
questions = open("questions.txt", "r")
questions_list = questions.read().rstrip().split('\n')

answers = open("answers.txt", "r")
answers_list = answers.read().rstrip().split('\n')

count = 0

for index, question in enumerate(questions_list):
    ask_question = input(question)
    if ask_question == answers_list[index]:
        print("Correct!")
        count += 1
print('Вы заработали: ' + str(count))
"""
Zadanie 5	
Создать словарь в качестве ключа которого будет 5-ти значное число, а в качестве значений кортеж состоящий из 2-ух элементов – имя(str) 
и возраста(int). Сделать 5-6 элементов словаря и записать данный словарь на диск в файл json формата
"""
import json
import csv

some_file = {"11111": {"name": "John", "age": 22},
             "22222": {"name": "Alice", "age": 23},
             "33333": {"name": "Max", "age": 26},
             "44444": {"name": "Sveta", "age": 25},
             "55555": {"name": "Bob", "age": 30},
             "66666": {"name": "Ann", "age": 28}}

with open("some_file.json", "w") as file_json:
    json.dump(some_file, file_json, indent=6)
file_json.close()
