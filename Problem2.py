def problem2():
    fib1 = 1
    fib2 = 1
    fib3 = 0
    result = 0

    while fib3 < 4000000:
        fib3 = fib1 + fib2
        if fib3 % 2 == 0:
            result += fib3

        fib1 = fib2
        fib2 = fib3

    return result


if __name__ == '__main__':
    print(problem2())
