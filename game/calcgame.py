from game import subjectivegame
import pyglet
from utils import maths


class CalcGame(subjectivegame.SubjectiveGame):

	operators = ['+', '-', '*', '/']

	def __init__(self, width, height):

		super().__init__('Calculate Game', width, height)

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

		self.lblExp.text = 'abcde'
		self.lblExp.draw()
		self.answer = '24'

		self.syncKey = False


	def genExpression(self):

		oprPDF = [0.35, 0.20, 0.30, 0.15]
		numRange = [(1,1) , (1,9) , (9,15) , (15,25)]
		numPDF = [0.01, 0.69, 0.27, 0.03]