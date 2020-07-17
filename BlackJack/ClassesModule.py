import random

ACE = 14
PRINCE = 11
KING = 13

class Deck():

	def __init__(self):

		self.cardsInDeck = createNewDeck()

	def drawCrad(self):

		return self.cardsInDeck.pop()

class CasinoUser():

	def __init__(self, name):
		self.name = name
		self.hand = Hand()

	def drawCard(self, deck):
		
		self.hand += deck.cardsInDeck.pop()
		#self.hand.cards.append(deck.cardsInDeck.pop())

class Player(CasinoUser):

	def __init__(self, name):
		super().__init__(name)
		self.chips = Chips()

	def placeBet(self, ammount):
		
		if ammount > self.chips:
			print("Not enough chips!")
		else:
			self.chips -= ammount

	def winBet(self, ammount):

		global pot
		self.chips = self.chips + pot.capacity
		pot.__init__()

	def emptyHand(self):

		self.hand = Hand()

class Dealer(CasinoUser):

	pass

class Chips():

	def __init__(self, ammount = 0):
		
		self.ammount = ammount

	def __sub__(self, number):

		self.ammount = self.ammount - number

		return self

	def __eq__(self, value):

		return self.ammount == value

	def __gt__(self, value):
		
		return self.ammount > value

	def __lt__(self, value):

		return self.ammount < value

	def __str__(self):

		return str(self.ammount)

	def __add__(self, other):

		if type(other) == type(self):
			self.ammount += other.ammount
		else:
			self.ammount += other

		return self

	def __isub__(self, value):

		self = self - value

		return self

	def __sub__(self, value):

		self.ammount -= value

		return self

	def __int__(self):

		return self.ammount


class Pot():

	def __init__(self):

		self.capacity = Chips(0)

	def emptyPot(self):

		self.capacity.ammount = 0

	def __add__(self, num):

		self.capacity = self.capacity + num

		return self

	def __str__(self):

		return str(self.capacity)

class Hand():

	def __init__(self):

		self.cards = []

	def __iadd__(self, value):

		self = self + value

		return self

	def __add__(self, value):

		self.cards.append(value)

		return self

	def __str__(self):

		return ', '.join(str(card) for card in self.cards)

def createNewDeck():

	deckLst = list(range(2, 15))
	for i in range(9, 13):
		if PRINCE <= deckLst[i] <= KING:
			deckLst[i] = 10
		elif deckLst[i] == ACE:
			deckLst[i] = 11
	deckLst *= 4
	random.shuffle(deckLst)

	return deckLst

def createHand():

	global deck
	hand = list(deck.pop())
	hand.append(deck.pop())
	
	return hand