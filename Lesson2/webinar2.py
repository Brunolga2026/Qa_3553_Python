# list(список) ...[1, "str", True, 3.8]
# ...упорядоченный, изменяемый, может хранить дубли

# tuple (1, "str", False)
# неизменяемый

# dict {"e": 2}
# словарь хранит уникальный неизменяемый ключ и значения (изменяемые, дубли)

# set {1,2, "try"}
# хранятся уникальные данные
from enum import unique

person = {
    "name": "Olga",
    "age": 22,
    "city": "Haifa",
}
print(person)

empty_dict = {}
print(empty_dict)

print("Count of keys: ", len(person))
print("Count of values: ", len(person.values()))

print(person["name"])
print(person["age"])
print(person["city"])

print(person.get("cita")) #найти ключ если его нет, код не упадет
print(person.get("cita", "not found")) # второе значение - это что выведется если не найден ключ

# добавить в словарь
person["phone"] = ('0123456789')
print(person)

# изменить значение
person["age"] = 33
print(person)

# удалить пару по ключу
del person["age"]
print(person)

# как еще проверить наличие ключа
print("name" in person)
print("email" not in person)

prices = {
    "apple": 100,
    "banana": 200,
    "orange": 300,
    "cherry": 400,
}
# вывести все ключи
for product in prices:
    print("Product: ", product)

# вывести значение в парах
for product, price in prices.items():
    print(f"Product: {product}, Price: {price}")

# список все ключей
print(list(prices.keys()))

# список всех значений
print(list(prices.values()))

# сумма всех значений
print(sum(prices.values()))

dict_any_types = {
    1: "paz",
    "two" : 2,
    (0,1): "rtfyt"}

# True это 1, False это 0
print((True, False) ==(1,0))
dict_any_types[(True, False)] = True
print(dict_any_types)
dict_any_types[(False, True)] = False # заменяmся ключи 0,1 на False, True, тк не уникальный
print(dict_any_types)

# ###################   SET   #########################
color = {"red", "green", "blue"}
numbers_set = {1,3,5,3,2,1,1,6,3}
print(numbers_set) # выводит только уникальные значения, нет порядка в хранении, не можем обратиться к индексам

empty_set = set() # пустой сет
print(empty_set)
print(type(empty_dict))
print(type(empty_set))

names = ["Olga", "Masha", "Dima", "Olga"]
print(names)
unique_names = set(names)
print(unique_names)

unique_names.add("Misha")
print(unique_names)

print("Olga" in names) # проверка включает ли сет значение

a = {1, 2, 3, 4}
b = {3, 6, 5, 6}
print(a | b) # объединение {1, 2, 3, 4, 5, 6}
print(a & b) # пересечение {3,4}
print(a - b) # разность {1,2}
print(b - a) # чем отличается b от a

english = {"Anna", "Vova", "Misha"}
russian = {"Misha", "Anna", "Sveta"}
print(english & russian)
print(english | russian)

phone_book = {"Sveta": "053-333-3333",
              "Masha": "053-444-3333"}

name = "Misha"
if name in phone_book:
    print(f"Phone {name}: {phone_book[name]}")
else:
    print(f"Number of {name} is not found")

products = {"milk": 2, "bread": 3, "meat": 4}
print(products["milk"])
products["salt"] = 5
print(products)
print(sum(products.values()))

wild = ["tiger", "camel", "cat", "lion", "puma"]
pet = ["cat", "dog", "mouse", "lion"]
print(set(wild) & set(pet))