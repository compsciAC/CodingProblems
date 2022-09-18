number = 2763

testValue = 2

while testValue < number:
	if number % testValue == 0:
		number /= testValue
		testValue -= 1
	testValue += 1

print(number)
