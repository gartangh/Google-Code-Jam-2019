A = int(input())

for a in range(A):
	N = int(input())
	programs = []
	for n in range(N):
		program = input()
		extended_program = program
		while len(extended_program) < 500:
			extended_program += program
		programs.append(extended_program)

	R = [False] * 500
	P = [False] * 500
	S = [False] * 500
	solution = ''
	found = False
	impossible = False
	for i in range(500):
		for program in programs:
			if not R[i] and program[i] == 'R':
				R[i] = True
			elif not P[i] and program[i] == 'P':
				P[i] = True
			elif not S[i] and program[i] == 'S':
				S[i] = True

			if R[i] and P[i] and S[i]:
				impossible = True
				break

		if impossible:
			break
		else:
			if R[i] and P[i]:
				solution += 'P'
			elif P[i] and S[i]:
				solution += 'S'
			elif S[i] and R[i]:
				solution += 'R'
			elif R[i]:
				solution += 'P'
				found = True
				break
			elif P[i]:
				solution += 'S'
				found = True
				break
			elif S[i]:
				solution += 'R'
				found = True
				break


			def loses(program):
				if program[i] == 'R' and solution[i] == 'P':
					return True
				elif program[i] == 'P' and solution[i] == 'S':
					return True
				elif program[i] == 'S' and solution[i] == 'P':
					return True
				return False


			programs = [program for program in programs if not loses(program)]

	if impossible or not found:
		print('CASE #' + str(a+1) + ': IMPOSSIBLE')
	elif found:
		print('CASE #' + str(a+1) + ': ' + solution)
