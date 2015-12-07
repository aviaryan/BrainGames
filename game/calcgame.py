# from game import subjectivegame
from game.subjectivegame import SubjectiveGame
import pyglet
from utils import maths


class CalcGame(SubjectiveGame):

	operators = ['+', '-', '*', '/']

	def __init__(self, width, height):

		super().__init__('Calculate Game', width, height, color = '#400000')

		self.gameTime = 45
		self.lblExp = pyglet.text.Label('2 + 4', x = self.width//2, anchor_x='center', y = self.description.y - 100, font_size = 20)
		self.addNew()
		self.beginPlay()


	def on_draw(self):
		self.window.clear()
		self.lblExp.draw()


	def on_text(self, text):
		if self.syncKey:
			return
		if text.isdigit():
			self.cText += text
			self.lblAnswer.text = self.cText
			if len(self.answer) == len(self.cText):
				self.submit()


	def addNew(self):
		self.syncKey = True

		size = maths.weightedRandomIndex([0.55, 0.35, 0.10]) + 2 # expr of size 2,3 or 4
		exp = self.genExpression(size)

		self.lblExp.text = exp[0]
		self.lblExp.draw()
		self.answer = str(exp[1])

		self.syncKey = False


	def genExpression(self, size):
		'''
		Generate the expression
		'''
		oprPDF = [0.35, 0.20, 0.30, 0.15]
		numRange = [(1,9) , (9,15) , (15,40)]
		numPDF = [0.6, 0.37, 0.13]

		if size == 2:
			exp = self.genExpression2(oprPDF)
		elif size == 3:
			exp1 = self.genExpression2(oprPDF)
			ans1 = eval(''.join(str(i) for i in exp1))
			opr = self.operators[ maths.weightedRandomIndex([0.4, 0.2, 0.3, 0.1]) ]
			exp2 = maths.getSecondOperand(ans1, opr, multiplyLimit = 200, numPDF = numPDF, numRange = numRange)
			exp = ['('] + exp1 + [')'] + [opr, exp2]
		elif size == 4:
			exp1 = self.genExpression2(oprPDF)
			exp2 = self.genExpression2(oprPDF)
			exp = ['('] + exp1 + [')'] + ['+'] + ['('] + exp2 + [')']

		expStr = ' '.join( str(i) for i in exp )
		return (expStr, round(eval(expStr)))


	def genExpression2(self, oprPDF):
		index = maths.weightedRandomIndex(oprPDF)
		numRange = [(1,9) , (9,15) , (15,40)]
		numPDF = [0.6, 0.37, 0.13]
		n1 = round(maths.weightedRandomRange(numPDF, numRange))
		opr = self.operators[index]
		n2 = maths.getSecondOperand(n1, opr, multiplyLimit = 100, numPDF = [0.2, 0.4, 0.3], numRange = numRange)
		if opr == '+':
			numPDF = [0.2, 0.4, 0.3]
			n1 = round(maths.weightedRandomRange(numPDF, numRange))

		return [n1, opr, n2]