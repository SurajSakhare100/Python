import math

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = 5
print(f"The factorial of {num} is {factorial(num)}")


def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

num = 17
if is_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")



def circle_area(radius):
    return math.pi * radius ** 2

radius = 5
print(f"The area of a circle with radius {radius} is {circle_area(radius)} square units.")


def fibonacci_sequence(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

num_terms = 10
print(f"The Fibonacci sequence up to {num_terms} terms is: {fibonacci_sequence(num_terms)}")
