
def rps():
	player1 = input('Player 1, choose (rock, paper or scissors): ')
	player2 = input('Player 2, choose: ')
	stats = [player1, player2]

	if stats[0] != stats[1]:
		if 'rock' in stats and 'paper' in stats:
			winner = stats.index('paper')

		if 'rock' in stats and 'scissors' in stats:
			winner = stats.index('rock')

		if 'paper' in stats and 'scissors' in stats:
			winner = stats.index('scissors')

	else:
		print('Draw!')

	if winner == 0: print('Player 1 wins!')
	elif winner == 1: print('Player 2 wins!')

	stats.clear()

	again = input('Do you want to play again? ')

	while again == '':
		again = input('Do you want to play again? ')

	if again == 'yes': rps()
	elif again == 'no': print('Thanks for playing!')


rps()





