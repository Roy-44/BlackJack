import ClassesModule
import locale

def askPlayerToChangeAceToOne(player):
	
	aceOccurrences = player.hand.cards.count(11)
	for i in range(len(player.hand.cards)):
		if player.hand.cards[i] == 11:
			toChange = ''
			while toChange not in ['Y', 'N']:
				if toChange != '':
					print('Invalid Input! Please Try Again')
				toChange = input('Would You Like To Change Ace To One? Type(Y/N) ').upper()
			if toChange == 'Y':
				player.hand.cards[i] = 1
			print('{} Hand: {}\n'.format(player.name, player.hand))

if __name__ == '__main__':
	locale.setlocale(locale.LC_ALL, '')
	deck = ClassesModule.Deck()
	pot = ClassesModule.Pot()
	dealer = ClassesModule.Dealer('Dealer');
	print('WELCOME TO ROY\'S CASINO!')
	print('- '*15)
	playerName = ''
	while playerName == '':
		playerName = input('Please Enter Your Name: ')
	player = ClassesModule.Player(playerName)
	invalidInput = True
	while invalidInput:
		try:
			player.chips.ammount = int(input('Please Enter Ammount Of Chips To Strat With: '))
		except:
			print('Invalid Ammount! Please Try Again')
		else:
			invalidInput = False
	gameOn = True
	while gameOn:
		deck = ClassesModule.Deck()
		dealer = ClassesModule.Dealer('Dealer')
		player.emptyHand()
		pot.emptyPot()
		print('***		{} Got {}		***'.format(player.name, locale.currency(player.chips.ammount, grouping = True)))
		print()
		invalidInput = True
		while invalidInput:
			try:
				bet = int(input('Place Bet: '))
			except:
				print('Invalid Ammount! Please Try Again')
			else:
				if player.chips < bet:
					print('Not Enough Chips! Please Try Again')
				else:
					invalidInput = False
		pot.capacity += (bet * 2)
		player.chips -= bet
		print('\n', '=	' * 10)
		dealer.drawCard(deck)
		dealer.drawCard(deck)
		player.drawCard(deck)
		player.drawCard(deck)
		print('Pot: {}'.format(locale.currency(pot.capacity.ammount, grouping = True)))
		print('Dealer\'s Hand: X, {}\n'.format(dealer.hand.cards[0]))
		print('{}\'s Hand: {}\n'.format(player.name, player.hand))
		print('***	{}\'s Turn	***'.format(player.name))
		askPlayerToChangeAceToOne(player)
		drawOrStay = ''
		while sum(player.hand.cards) < 21 and drawOrStay != 'S':
			drawOrStay = ''
			while drawOrStay not in ['D', 'S']:
				if drawOrStay != '':
					print('Invalid Input! Please Try Again')
				drawOrStay = input('Do You Want To Draw Another Card Or Stay? (Type D/S) ').upper()
			if drawOrStay == 'S':
				print('***	Your Turn Has Ended!	***\n')
			else:
				player.drawCard(deck)
			print('{} Hand: {}\n'.format(player.name, player.hand))
			if drawOrStay == 'D':
				askPlayerToChangeAceToOne(player)
		if sum(player.hand.cards) > 21:
			print('***	You Are Burn!	***')
		else:
			print('Dealer Hand: {}\n'.format(dealer.hand))
			dealerSum = sum(dealer.hand.cards)
			if dealerSum > 21 and 11 in dealer.hand.cards:
				dealer.hand.cards[dealer.hand.cards.index(11)] = 1
				dealerSum -= 10
				print('Dealer Changed Ace To One')
				print('Dealer Hand: {}\n'.format(dealer.hand))
			while (dealerSum < 21) and (dealerSum <= sum(player.hand.cards)):
				dealer.drawCard(deck)
				print('Dealer Hand: {}\n'.format(dealer.hand))
				dealerSum += dealer.hand.cards[-1]
				if dealerSum > 21 and 11 in dealer.hand.cards:
					dealer.hand.cards[dealer.hand.cards.index(11)] = 1
					dealerSum -= 10
					print('Dealer Changed Ace To One')
					print('Dealer Hand: {}\n'.format(dealer.hand))
			if dealerSum > 21:
				print('\n***	You Won!	***')
				player.chips += pot.capacity
			else:
				print('\n***	You Lost!	***')
		print('***		{} Got {}		***'.format(player.name, locale.currency(player.chips.ammount, grouping = True)))
		if player.chips.ammount == 0:
			break
		anotherGame = ''
		while anotherGame not in ['Y', 'N']:
			if anotherGame != '':
				print('Invalid Input! Please Try Again')
			anotherGame = input('Would You Like To Have Another Game? (Type Y/N) ').upper()
		if anotherGame == 'N' or player.chips.ammount == 0:
			gameOn = False
	print('\n\n\n')
	print('\n*****	You Left The Casino With {}	*****\n\n\n'.format(locale.currency(player.chips.ammount, grouping = True)))
	input('Press Enter To Exit...')