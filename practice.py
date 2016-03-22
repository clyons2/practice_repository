for n in range(25):
	if n % 3 == 0:
		if n % 5 == 0:
			print('FizzBuzz')
		print('Fizz')
	if n % 5 == 0:
		print('Buzz')
		
print('Edit')

def FizzBuzz(x):
	for n in range(x):
		if n % 3 == 0:
			if n % 5 == 0:
				print('FizzBuzz')
			print('Fizz')
		if n % 5 == 0:
			print('Buzz')
			
print(FizzBuzz(200))
