T = int(input())
for i in range(T):
	N = int(input())
	L = input()
	O = ''
	for j in range(2 * N - 2):
		if L[j] == 'S':
			O += 'E'
		else:
			O += 'S'
	print('Case #' + str(i + 1) + ': ' + O)
