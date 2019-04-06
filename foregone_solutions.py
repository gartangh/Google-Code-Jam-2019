T = int(input())
for i in range(T):
	N = int(input())
	N_string = str(N)
	A_string = ''
	for c in N_string:
		if c == '4':
			A_string += '2'
		else:
			A_string += c
	A = int(A_string)
	B = N - A
	print('Case #' + str(i + 1) + ': ' + str(A) + ' ' + str(B))
