user_input = input('Введитие выражение: ')
user_input
a = int()
b = int()

def function_1(a,b):
    return a*b

def function_2(a,b):
    return a+b

def function_3(a,b):
    return a-b 

def function_4(a,b):
    return a/b

def separate(string: str, separator):
    result = string.split(separator)
    for i in range(0, len(result)):
        result[i] = int(result[i])
    return string.split(separator)

if "+" in user_input:
    numbers = separate(user_input, "+")
    print(function_2(numbers[0], numbers[1]))

elif "-" in user_input:
    numbers = separate(user_input, "-")
    print(function_3(numbers[0], numbers[1]))

elif "*" in user_input:
    numbers = separate(user_input, "*")
    print(function_1(numbers[0], numbers[1]))

elif "/" in user_input:
    numbers = separate(user_input, "/")
    print(function_4(numbers[0], numbers[1]))

else:
    print('Не правильный ввод')













