def mult(a, b):
    return a * b

def summa(a, b):
    return a + b

def sub(a, b):
    return a - b 

def div(a, b):
    if b == 0:
        return "Ошибка: деление на ноль"
    return a / b

def separate(string: str, separator):
    result = string.split(separator)
    return [int(x) for x in result]  # Преобразование в список чисел

user_input = input('Введите выражение: ')

if "+" in user_input:
    numbers = separate(user_input, "+")
    print(summa(numbers[0], numbers[1]))

elif "-" in user_input:
    numbers = separate(user_input, "-")
    print(sub(numbers[0], numbers[1]))

elif "*" in user_input:
    numbers = separate(user_input, "*")
    print(mult(numbers[0], numbers[1]))

elif "/" in user_input:
    numbers = separate(user_input, "/")
    print(div(numbers[0], numbers[1]))

else:
    print('Неправильный ввод')
