numbers = range(1, 101)
sumSquared = sum(numbers)**2
sumOfSquares = sum([i**2 for i in numbers])
print(sumSquared - sumOfSquares)
