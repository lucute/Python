#StressTest.py

def MaxProduct(numbers):
	n = len(numbers)
	product = 0
	for i in range(n):
		for j in range(i + 1, n):
			product = max(product, numbers[i] * numbers[j])

	return product


def MaxProductFast(numbers):
	n = len(numbers)
	product = 0
	index1 = 0
	for i in range(1,n):
		if numbers[i] > numbers[index1]:
			index1 = i
	if index1 == 0:
		index2 = 1
	else:
		index2 = 0
	for i in range(0,n):
		if (i != index1) & (numbers[i] > numbers[index2]):
			index2 = i
	product = numbers[index1] * numbers[index2]

	return product


import random

def StressTest(N,M):
	while True:
		n = random.randint(2,N)
		A = [0]*n
		for i in range(0,n-1):
			A[i] = random.randint(0,M)
		print(A)
		result1 = MaxProduct(A)
		result2 = MaxProductFast(A)
		if result1 == result2:
			print('Yes!')
		else:
			print('Oops:'+ str(result1) + ' ' + str(result2))

	return

if __name__ == '__main__':
	inputs = [int(x) for x in input().split()]
	N = inputs[0]
	M = inputs[1]
	print(StressTest(N,M))

