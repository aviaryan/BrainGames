from game import boolgame
import pyglet
from utils import maths


class MathGame(boolgame.BoolGame):

	comparators = ['==', '<', '>']
	operators = ['+', '-', '*', '/']


	def __init__(self, width, height):

		self.negative = -10 # tryin to be fair

		super().__init__('Math Game', width, height, description='Check if the expression is true or not')

		self.lblExp = pyglet.text.Label('2 < 4', font_size=20, x = self.width//2, y = self.description.y - 100, anchor_x = 'center', anchor_y = 'center')
		self.lblExp.draw()


	def game_on_draw(self):
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
		leftSize = maths.weightedRandomIndex([0.15, 0.75]) + 1
		rightSize = maths.weightedRandomIndex([0.2, 0.8]) + 1

		lhs = self.getExpression(leftSize)
		rhs = self.getExpression(rightSize)

		ans = eval( '(' + lhs + ')' + 
					self.comparators[chComparator] +
					'(' + rhs + ')' 
				)

		return (lhs + '  ' + self.comparators[chComparator].replace('==', '=') + '  ' + rhs , ans)


	def getExpression(self, size):
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
		if opr == '/':
			factors = maths.factors(n1)
			choice = maths.randint(0, len(factors)-1)
			n2 = factors[choice]
		else:
			n2 = round(maths.weightedRandomRange(numPDF, numRange))

		return str(n1) + ' ' + opr + ' ' + str(n2)