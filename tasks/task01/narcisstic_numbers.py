for n in range(1, 1001):
    digits = 0
    i = n
    while i > 0:
        i = i // 10
        digits += 1

    hundreds = n // 100  # first number or 0
    tens = (n - hundreds * 100) // 10  # second number or 0
    ones = n % 10

    if n == hundreds ** digits + tens ** digits + ones ** digits:
        print(n)
