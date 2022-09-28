from math import ceil, log

def primeNumbers(limit):
    primeList = [2]
    isNotPrime = set()
    for i in range(3, limit, 2):
        if i in isNotPrime:
            continue

        for j in range(i*3, limit, i*2):
            isNotPrime.add(j)

        primeList.append(i)
    return primeList

def primeLimit(number):
    return ceil(number * (log(number) + log(log(number))))

def nthPrime(number):
    primes = list(primeNumbers(primeLimit((number+1))))
    return primes[number - 1]
    
