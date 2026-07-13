text1 = "I want to say \"Hi\""
print(text1)
text2 = "First string\nSecond string\nThird string"
print(text2)

print(len(text2))

first_name = "Olga"
last_name = "Brun"
full_name = first_name + ' ' + last_name
print(full_name)
long_string = 'Uh ' *5
print(long_string)
city = 'Haifa'
temperature = 28.5
text = f"Today in {city} thr temperature is {temperature}"
print(text)
print(f"Tommorow will be : {temperature + 3}")
print(f"Name is uppercase: {first_name.upper()}")

word = 'Privet'
print(word[0])
print(word[-1])
print(word[0:4])
print(word[2:])
print(word[2:len(word)])
print(word[:2])
print(word[::-1])

example_text = '  I like walking   '
print(example_text.upper())
print(example_text.lower())
print("example_text".capitalize())
print(example_text.title())

print(example_text.strip())
print(example_text.lstrip())
print(example_text.rstrip())
print(example_text.strip().replace('walking', 'hiking'))

text6 = "I like swimming"
parts = text6.split(" ") # режем методом list
print(parts)
print(" ,".join(parts))

print(text6.find('swimming')) # с какого индекса слово начинается

print("mamammaama".count("a"))
print("1234".isdigit()) # проверка внутри строки только цифры
print("wert".isalpha()) # проверка внутри строки только буквы

raw = " Today is a good day  "
print(raw.strip().replace(" ", "***"))

date_str = "09.07.2026"
day, month, year = date_str.split(".")
print(f"Год: {year}, Месяц: {month}, День: {day}")








