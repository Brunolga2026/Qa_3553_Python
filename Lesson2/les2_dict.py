from http.client import responses

books = {
    'Happy Potter and.....':'J.K. Rowling',
    'To kill a mockimgbird':'Harper Lee'
}

books1 = {
'Happy Potter and.....',
    'To kill a mockimgbird'
}

print(books1)

response = {
    'status':'success',
    'user':{'id':1, 'name':'Olga'}
}

print(response['user']['name'])

data = [1,22,3]
print(isinstance(data,list))

value = 10.
print(type(value))
print(isinstance(value, (int,float)))

team_ages = {
    "Alex":23,
    "Viki":42,
    "Petr":52,
    "Den":32,
    "Olga":26
}
print(team_ages.keys())
print(team_ages.values())

# zip - преобразует 2 списка в список кортежей, по которому выполняется итерация в цикле for
team_names = ["Alex", "Viki", "Petr", "Den", "Olga"]
team_numbers = [23, 42, 52, 32, 26]
team_ages = {name:age for name, age in zip(team_names, team_numbers)}
print(team_ages)