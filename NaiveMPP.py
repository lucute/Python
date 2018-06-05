# Uses python3



def MaxProduct(numbers):
	n = len(numbers)
	product = 0
	for i in range(n):
		for j in range(i + 1, n):
			product = max(product, numbers[i] * numbers[j])

	return product


if __name__ == '__main__':
	input_n = int(input())
	input_numbers = [int(x) for x in input().split()]
	print(MaxProduct(input_numbers))