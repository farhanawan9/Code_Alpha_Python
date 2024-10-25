def fibonacci_generator(limit):
    """Generate Fibonacci numbers up to the specified limit."""
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


limit = 100  
print(f"Fibonacci series up to {limit}:")
for number in fibonacci_generator(limit):
    print(number)
