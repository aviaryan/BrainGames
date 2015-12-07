from game.choicegame import ChoiceGame, Choice
from random import shuffle, randint
from utils import maths


class Scrabble(ChoiceGame):

	def __init__(self, width, height):

		self.data = loadWordlist()

		super().__init__('Word Scrabble', width, height, color = '#004040')

		self.addNew()
		self.beginPlay()


	def addNew(self):

		self.syncKey = True
		#     [5, 6, 7, 8, 9, 10]
		pdf = [0.2, 0.3, 0.2, 0.1, 0.1, 0.1]
		wlen = maths.weightedRandomIndex(pdf) + 5
		pos = randint(0, len(self.data[wlen])-1)
		word = self.data[wlen][pos]
		scrabbled = scrabbleWord(word).upper()
		self.answer = randint(1,4)
		self.lblQuestion.text = scrabbled

		self.syncKey = False


	def on_draw(self):
		self.window.clear()



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
	# https://github.com/ManiacDC/TypingAid
	
	data = dict()
	for i in range(5,10+1):
		data[i] = []
	path = 'resources/WordList.txt'
	with open(path) as f:
		for line in f:
			if not line[:-1].isalpha():
				continue
			line = line.strip()
			if len(line) > 4 and len(line) < 11:
				data[len(line)] += [line]
	return data