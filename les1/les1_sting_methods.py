name = 'Alice'
age = 30

formatted_string = f"Hello my name is {name} and I am {age} years old"
print(formatted_string)

#find()
s = 'AbrakadabraAbrakadabra'
str = 'bra'
print(s.find(str)) #если находит показывает первый встречный индекс
print(s.rfind(str)) # показывает все что совпало
print(s.find('add'))
#*************************
#count(sub[start,end])
print(s.count(str))
print(s.count(str,4))

#str.upper()
#str.lower()
s = 'AbraaDabRaAbrakaDabra'
print(s.lower())
print(s.upper())
print(s)

#*************************
#split()
s = 'Cat, Dog,Hamster  Rabbit, Pig'
print(s.split())
print(s.split(','))
print(s.split(',',2))

#*******************
#rjust() & ljust()
s = 'Hi!'
print(s.rjust(10, '*'))
print(s.ljust(10, '*'))

test = ["Login", "Cart", "API"]
for t in test:
    print(t.ljust(15), "OK")

order = "125"
print(order.rjust(8, "0"))

order = "125"
print(order.rjust (8, "0"))
#******************
s = 'AbraaDabRaAbrakaDabra'
print(s.isalpha())
s1 = "123456"
print(s.isdigit())
print(s1.isdigit())

#********************
#index()
text = "QA automation with Python"
pos = text.index("automation")
print(pos)

#replace()
text = 'I like Java'
print(text.replace("Java", "Python"))

text = "2026-07-03"
new_text = text.replace("-", "/")
print(text)
print(new_text)

