def print_fibonacci(length):
    fibonacci_sequence = []

    if length <= 0:
        print([])
        return

    a, b = 0, 1

    for _ in range(length):
        fibonacci_sequence.append(a)
        a, b = b, a + b

    print(fibonacci_sequence)  
