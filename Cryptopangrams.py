import numpy as np

T = int(input())
for i in range(T):
	N, L = map(int, input().split())
	C = list(map(int, input().split()))

	primes = []
	ME = []

	for j in range(L - 1):
		gcd = np.gcd(C[j], C[j + 1])
		if gcd not in primes:
			primes.append(gcd)
		if C[j] / gcd not in primes:
			primes.append(C[j] / gcd)
		if C[j + 1] / gcd not in primes:
			primes.append(C[j + 1] / gcd)

		ME.append(C[j] / gcd)
		if j == L - 2:
			ME.append(gcd)
			ME.append(C[j + 1] / gcd)

	primes = np.sort(primes).tolist()

	MU = ''
	for j in ME:
		MU += chr(65 + primes.index(j))

	print('Case #' + str(i + 1) + ': ' + MU)
