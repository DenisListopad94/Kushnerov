#exercise 1
import re

s = "The cat sleep"

all_matches = re.findall(r'\b\w*cat\w*\b', s)

for match in all_matches:
    print(match)
#exercise 2
import re

s = "Zebra svnos zzz zebra"

pattern = r'z.{3}z'

all_matches = re.findall(pattern, s)

for match in all_matches:
    print(match)
#exercise 3
import re

phone_numbers = [
    "8675309000",
    "1234567890",
    "9876543210",
    "9998887776",
    "8123456789"
]

pattern = r'^[89]\d{9}$'

for phone_number in phone_numbers:
    if re.match(pattern, phone_number):
        print(f"Номер {phone_number} соответствует условиям.")
    else:
        print(f"Номер {phone_number} не соответствует условиям.")
#exercise 4

import re

s = "Эта строка содержит несколько слов, начинающихся на гласные: апельсин, огурец, утка, ирис, ежевика."

vowels = 'aeiouаеёиоуыэюя'
regular_expression = r'\b[{}AEIOUАЕЁИОУЫЭЮЯ][a-zA-Zа-яА-ЯёЁ]*\b'.format(vowels)

occurrences = re.findall(regular_expression, s, re.IGNORECASE)

for word in occurrences:
    print(word)

#exercise 5
import re

s = "Это строка содержит числа: 42, -17, 3.14, 1000, -5."

regular_expression = r'-?\d+\.?\d*'

numbers = re.findall(regular_expression, s)

for numb in numbers:
    print(numbers)
#exercise 6
import re

str = [
    "This is a human development.",
    "Humans are evolving.",
    "The study of human behavior is important."
]

for elem in str:
    new_string = re.sub(r'human', 'computer', elem)
    print(new_string)
#exercise 7
import re

# Строка, содержащая дату
text = "Сегодня 28-02-2022"

# Используем регулярное выражение для извлечения даты в формате dd-mm-yyyy
date_pattern = r'(\d{2}-\d{2}-\d{4})'
match = re.search(date_pattern, text)

if match:
    extracted_date = match.group(1)
    print("Извлеченная дата:", extracted_date)
else:
    print("Дата не найдена в тексте.")
#exercise 8
import re

# Строка, в которой нужно найти слова с буквой 'b'
text = "Слова с буквой b: bob, abc, banana, cab, none"

# Используем регулярное выражение для поиска слов с буквой 'b'
word_pattern = r'\b\w*b\w*\b'
matched_words = re.findall(word_pattern, text)

print("Слова с буквой 'b':", matched_words)