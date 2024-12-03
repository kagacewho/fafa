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

def calculate(expression):
    # Шаг 1: Обработка умножения и деления
    while "*" in expression or "/" in expression:
        tokens = expression.split()
        for i in range(len(tokens)):
            if tokens[i] == "*":
                result = mult(int(tokens[i - 1]), int(tokens[i + 1]))
                tokens = tokens[:i-1] + [str(result)] + tokens[i+2:]
                break
            elif tokens[i] == "/":
                result = div(int(tokens[i - 1]), int(tokens[i + 1]))
                tokens = tokens[:i-1] + [str(result)] + tokens[i+2:]
                break
        expression = " ".join(tokens)

    # Шаг 2: Обработка сложения и вычитания
    while "+" in expression or "-" in expression:
        tokens = expression.split()
        for i in range(len(tokens)):
            if tokens[i] == "+":
                result = summa(int(tokens[i - 1]), int(tokens[i + 1]))
                tokens = tokens[:i-1] + [str(result)] + tokens[i+2:]
                break
            elif tokens[i] == "-":
                result = sub(int(tokens[i - 1]), int(tokens[i + 1]))
                tokens = tokens[:i-1] + [str(result)] + tokens[i+2:]
                break
        expression = " ".join(tokens)

    return expression

# Пример работы
user_input = input("Введите выражение (разделяйте пробелами, например, '2 + 3 * 4 - 5'): ")
print("Результат:", calculate(user_input))














