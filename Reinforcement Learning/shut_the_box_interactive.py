import random
flags = {i for i in range(1, 10)}
# print(flags)
input('Game start. Press enter to continue')

def calc_sum(flags):
	s = 0
	for i in flags:
		s += i
	return s

total_sum = calc_sum(flags)

while True:
	print('Numbers left:', end='')
	for i in range(1, 10):
		if i in flags:
			print(i, end=' ')
	print()

	dice1 = random.randint(1, 6)
	dice2 = random.randint(1, 6)

	print('You have rolled %d and %d this turn. Summation is %d.' % (dice1, dice2, dice1+dice2))

	user_input = input('Give the numbers that you want to shut this turn (put only numbers seperate them by comma), or give up:')
	
	s = 0
	not_terminated = True
	temp_flags = flags.copy()

	for nbs in user_input.split(','):
		if not nbs.strip().isdigit():
			not_terminated = False
			break
		else:
			nb = int(nbs.strip())
			if nb in temp_flags:
				temp_flags.remove(nb)
				s += nb
			else:
				not_terminated = False
				break


	if not not_terminated or s!=dice1+dice2:
		print('Game terminated.')
		break
	else:
		flags = temp_flags
		if len(flags) == 0:
			print('You have shut the box!')
			break

print('Your total reward', total_sum - calc_sum(flags))
