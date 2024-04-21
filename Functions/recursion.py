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

