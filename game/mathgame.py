from game import boolgame
import pyglet
from utils import maths


class MathGame(boolgame.BoolGame):

	comparators = ['==', '<', '>']
	operators = ['+', '-', '*', '/']


	def __init__(self, width=600, height=500):

		super().__init__('Math Game', width, height, color = '#004000')

		self.gameid = 'mathgame'
		self.negative = -10 # tryin to be fair
		self.lblExp = pyglet.text.Label('..', font_size=20, x = self.width//2, y = self.description.y - 100, anchor_x = 'center', anchor_y = 'center')
		self.window.dispatch_event('on_key_press', 21, '') # start the game, no need for description


	def on_draw(self):
		'''
		Default on_draw event for the game
		'''
		self.window.clear()
		self.lblExp.draw()


	def addNew(self):

		self.syncKey = True

		exp = self.genInequality()
		self.lblExp.text = exp[0]
		self.lblExp.draw()
		self.answer = exp[1]

		self.syncKey = False


	def genInequality(self):
		'''
		Generates a random inequality for this game
		'''
		chComparator = maths.weightedRandomIndex([0.24, 0.38, 0.38])
		leftSize = maths.weightedRandomIndex([0.15, 0.85]) + 1
		rightSize = maths.weightedRandomIndex([0.15, 0.85]) + 1

		lhs = self.genExpression(leftSize)
		rhs = self.genExpression(rightSize)

		ans = eval( '(' + lhs + ')' + 
					self.comparators[chComparator] +
					'(' + rhs + ')' 
				)

		return (lhs + '  ' + self.comparators[chComparator].replace('==', '=') + '  ' + rhs , ans)


	def genExpression(self, size):
		'''
		generates an expression
		'''
		oprPDF = [0.35, 0.20, 0.30, 0.15]
		numRange = [(1,1) , (1,9) , (9,15) , (15,25)]
		numPDF = [0.01, 0.69, 0.27, 0.03]

		n1 = round(maths.weightedRandomRange(numPDF, numRange))
		if size == 1:
			return str(n1)
		if size > 2:
			print('Not implemented')
		# size = 2
		opr = self.operators[ maths.weightedRandomIndex(oprPDF) ]
		n2 = maths.getSecondOperand(n1, opr, multiplyLimit = 300, numPDF = numPDF, numRange = numRange)

		return str(n1) + ' ' + opr + ' ' + str(n2)