with open ("users.txt", "w", encoding="utf-8") as file:
    file.write("tony\n")
    file.write("ivan\n")
    file.write("anna\n")

    #read() - метод читает весь файл целиком
with open("users.txt", "r", encoding="utf-8") as file:
    content = file.read()
print(content)
print(len(content))

    # readlined() - возвращает список, где каждый элемент - 1 строка файла

with open("users.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

print(lines)

for line in lines:
    print(line.strip())

print()

with open("users.txt", "r", encoding="utf-8") as file:
    for lines in file:
        print(line.strip())

