def factorial(number):
    product = 1
    for i in range(1, number + 1):
        product *= i
    return product

def recursive_factorial(number):
    if number <= 1:
        return 1
    return number * recursive_factorial(number - 1)

def fibinacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    while n > 2:
        c = a + b
        a = b
        b = c
        n -= 1
    return c

def recursive_fibinacci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1

    return recursive_fibinacci(n - 1) + recursive_fibinacci(n - 2)

print(recursive_fibinacci(9))