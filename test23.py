def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage
number = 5
fact = factorial(number)
print(f"The factorial of {number} is: {fact}")
