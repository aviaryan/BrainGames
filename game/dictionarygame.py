from game.choicegame import ChoiceGame, Choice
from game.quesgame import QuesGame
import json
from random import randint
from pyglet.clock import schedule_once


class DictionaryGame(QuesGame, ChoiceGame):

	title = 'Dictionary Game'
	color = '#0C276C'
	descriptiontext = 'Choose the word which means the same as text provided'
	gameid = 'dictionary'

	def __init__(self, width=700, height=550):

		self.dic = loadDictionary()
		self.wlist = []
		for i in self.dic:
			self.wlist += [(i, self.dic[i])]

		ChoiceGame.__init__(self, self.title, width, height, color=self.color)
		QuesGame.__init__(self, numQuestions = 10)
		self.lblQuestion.font_size = 12
		self.lblQuestion.width = self.width - 100
		self.lblQuestion.multiline = True
		self.negative = 0

		self.loadGameSettings()
		self.quesLeft = self.numQuestions
		self.gameTime = self.numQuestions # load after gamesettings as gameTime is not a game variable for this game

		choice_y = self.lblQuestion.y - 80
		self.choice1 = Choice('Choice 1', 0, self.width//2 - 100, choice_y )
		self.choice2 = Choice('Choice 2', 1, self.width//2 - 100, choice_y - 60 )
		self.choice3 = Choice('Choice 3', 2, self.width//2 - 100, choice_y - 120 )
		self.choice4 = Choice('Choice 4', 3, self.width//2 - 100, choice_y - 180 )
		self.choices = [self.choice1, self.choice2, self.choice3, self.choice4]

		self.addNew()
		self.beginPlay(autotime = False)


	def showAnswer(self, status):
		'''
		show the correct answer to the user
		'''
		self.choices[ self.answer ].changecolor( [0,255,0] )
		schedule_once(self.undo_showAnswer, 0.6 if status else 1.1)


	def undo_showAnswer(self, dt):
		'''
		undo the showAnswer and then resume thread
		'''
		self.choices[ self.answer ].changecolor()
		if self.quesLeft == 0:
			self.endGame()
		self.updateTime()
		self.addNew()


	def addNew(self):
		'''
		add a new question
		'''
		self.syncKey = True
		self.quesLeft -= 1

		size = len(self.wlist)
		ques = 'a' * 500
		while len(ques) > 250:
			pQues = randint(0, size-1)
			ques = self.wlist[pQues][1]
		self.lblQuestion.text = ques
		self.answer = randint(0,3)
		for i in range(4):
			if i == self.answer:
				self.choices[i].label.text = self.wlist[pQues][0]
			else:
				pos = pQues
				while pos == pQues:
					pos = randint(0, size-1)
				self.choices[i].label.text = self.wlist[pos][0]

		self.syncKey = False



def loadDictionary():
	'''
	loads the dictionary
	'''
	fname = 'resources/dictionary_minimal.json'
	data = open(fname, 'r', encoding = 'utf-8').read()
	dic = json.loads(data)
	dic2 = dict(dic)
	for i in dic:
		j = i
		fail = 0
		c = 0
		while dic[j].startswith('___'):
			j2 = dic[j][3:]
			c+=1
			if j2 not in dic or j2 == j or c > 10:
				fail = 1
				break
			j = j2
		if fail == 1:
			del dic2[i]
		else:
			dic2[i] = dic2[j]
	return dic2