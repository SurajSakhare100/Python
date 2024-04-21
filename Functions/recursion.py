def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

number = 5
result = factorial(number)
print(f"The factorial of {number} is: {result}")


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

number = 6
result = fibonacci(number)
print(f"The {number}th Fibonacci number is: {result}")

def sum_of_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)

number = 12345
result = sum_of_digits(number)
print(f"The sum of digits of {number} is: {result}")

def sum_of_integers(n):
    if n == 1:
        return 1
    else:
        return n + sum_of_integers(n - 1)

number = 5
result = sum_of_integers(number)
print(f"The sum of integers from 1 to {number} is: {result}")

def reverse_string(string):
    if len(string) == 0:
        return string
    else:
        return reverse_string(string[1:]) + string[0]

text = "Hello, world!"
reversed_text = reverse_string(text)
print(f"The reversed string of '{text}' is: '{reversed_text}'")
