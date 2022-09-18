number = 600851475143
testValue = 2

while testValue < number:
	if number % testValue == 0:
		number /= testValue
		testValue -= 1
	testValue += 1
return number
