def print_fibonacci(n):
    fib = []

    if n <= 0:
        print(fib)
        return

    a, b = 0, 1
    for _ in range(n):
        fib.append(a)
        a, b = b, a + b

    print(fib)
