# Uses python3


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
		if numbers[i]!= numbers[index1] & numbers[i] > numbers[index2]:
			index2 = i

	product = numbers[index1] * numbers[index2]

	return product


if __name__ == '__main__':
	input_n = int(input())
	input_numbers = [int(x) for x in input().split()]
	print(MaxProductFast(input_numbers))