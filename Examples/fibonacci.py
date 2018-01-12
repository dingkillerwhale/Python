# Fibonacci numbers module

def fib(n): # enter how many numbers to get
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result
    
