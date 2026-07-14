from email.contentmanager import set_text_content

from Lesson1.webinar1 import first_name

empty_list = []
mixed = [2, 'orange', 4.22, True]

fruits = ['orange', 'peach', 'lemon']
print(fruits[0]) #индекс в списке

fruits[1] = 'blueberry' # замена элемента
print(fruits)

list1 = ['orange', 'peach']
list2 = ['shampoo', 'soap']
comb_list = list1+list2
print(comb_list)

fruits = ['orange', 'peach', 'lemon'] # присвоение элементу списка значения
first, second,third = fruits
print(first)
print(second)
print(third)

fruits = ['orange', 'peach', 'lemon']
for item in fruits:
    print(f"item in fruits: {item}")

correct_answers = ['orange', 'peach', 'lemon']
user_answers = ['orange', 'peach', 'apple']
if correct_answers == user_answers:
    print("All answers are correct!")
else:
    print("Some answers are incorrect")

print(len(fruits))
print()

numbers = [12,56,94,6]
print(max(numbers))
print(min(numbers))
print()

# Sorted - функция, возвращает новый список и работает с разными коллекциями, сортирует список
res = sorted(numbers)
print(res)
print(numbers)

#сортировка наоборот
print(sorted(numbers, reverse=True))
print(sorted(fruits, reverse=True))

word = 'pyThon'
print(sorted(word))
result = ''.join(sorted(word))
print(result)

names = ['Alexandr', 'Bob', 'Tom']
print(sorted(names))
print(sorted(names, key=len))

# sort - метод только списка, меняет список и ничего не возвращает

fruits = ['orange', 'peach', 'lemon']
fruits.append("orange") # добавить в конец
print(fruits)

fruits.insert(1, 'apple') # добавление элемента в нужрное место
print(fruits)

first_peach_index = fruits.index('peach')
print(f"The first 'peach' was added to position: {first_peach_index} ")

fruits.remove('orange') #удаляет по значению, ничего не возвр
print(fruits)

fruits.pop(2) #удаляет по индексу, возвращает удаленный элемент
print(fruits)

numbers1 = [10,20,30]
deleted = numbers1.pop(1)
print(deleted)
print(numbers1)
numbers1.clear()
print(numbers1)

