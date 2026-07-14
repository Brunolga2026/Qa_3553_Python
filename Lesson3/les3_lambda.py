from sys import base_prefix


def double(x):
    return x*2

# то же самое через лямбду
double_lambda = lambda x: x*2


print(double(5))
print(double_lambda(5))

print()

add = lambda a,b: a+b
print(add(3,4))

is_even = lambda n: n%2 ==0
print(is_even(10))
print(is_even(7))

