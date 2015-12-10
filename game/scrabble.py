from game.choicegame import ChoiceGame, Choice
from random import shuffle, randint
from utils import maths


class Scrabble(ChoiceGame):

	def __init__(self, width=700, height=500):

		self.gameid = 'scrabble'
		self.data = loadWordlist()

		super().__init__('Word Scrabble', width, height, color = '#004040')

		self.negative = -10
		self.loadGameSettings()

		choice_y = self.lblQuestion.y - 30
		self.choice1 = Choice('Choice 1', 0, self.width//2 - 100, choice_y )
		self.choice2 = Choice('Choice 2', 1, self.width//2 - 100, choice_y - 60 )
		self.choice3 = Choice('Choice 3', 2, self.width//2 - 100, choice_y - 120 )
		self.choice4 = Choice('Choice 4', 3, self.width//2 - 100, choice_y - 180 )
		self.choices = [self.choice1, self.choice2, self.choice3, self.choice4]

		self.addNew()
		self.beginPlay()


	def addNew(self):

		self.syncKey = True
		#     [5, 6, 7, 8, 9, 10]
		pdf = [0.3, 0.4, 0.15, 0.05, 0.05, 0.05]
		wlen = maths.weightedRandomIndex(pdf) + 5
		pos = randint(0, len(self.data[wlen])-1)
		word = self.data[wlen][pos]
		scrabbled = scrabbleWord(word)
		while word == scrabbled:
			scrabbled = scrabbleWord(word)
		self.answer = randint(0,3)
		poss = [pos]
		leftPoint = 0 if (pos-5 < 0) else pos-5
		rightPoint = len(self.data[wlen]) - 1 if (pos + 5 > len(self.data[wlen]) - 1) else pos + 5

		for i in range(4):
			if i == self.answer:
				self.choices[i].label.text = word.upper()
			else:
				pos = poss[0]
				while pos in poss or checkAnagram(self.data[wlen][pos], word) == True:
					pos = randint(leftPoint, rightPoint)
				self.choices[i].label.text = self.data[wlen][pos].upper()
				poss += [pos]


		self.lblQuestion.text = scrabbled.upper()
		self.syncKey = False


	def on_draw(self):
		self.window.clear()
		for _ in self.choices:
			_.draw()



def checkAnagram(word1, word2):
	'''
	check if two words are anagram of one another
	'''
	w1 = ''.join(sorted(word1)).upper()
	w2 = ''.join(sorted(word2)).upper()
	return w1 == w2


def scrabbleWord(word):
	'''
	scrabbles / shuffles a word
	'''
	word = list(word)
	shuffle(word)
	return ''.join(word)



def loadWordlist():
	'''
	loads the wordlist into an array
	'''
	# Wordlist_3600 https://github.com/ManiacDC/TypingAid
	# corncob_caps http://www.mieliestronk.com/wordlist.html

	data = dict()
	for i in range(5,10+1):
		data[i] = []
	path = 'resources/corncob_caps.txt'
	with open(path) as f:
		for line in f:
			if not line[:-1].isalpha():
				continue
			line = line.strip()
			if len(line) > 4 and len(line) < 11:
				data[len(line)] += [line]
	return data