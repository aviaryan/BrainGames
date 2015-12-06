from game import subjectivegame
import pyglet
from pyglet.window import key


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
		if text.isdigit():
			self.cText += text
			self.lblAnswer.text = self.cText


	def addNew(self):
		self.syncKey = True

		self.lblExp.text = 'abcde'
		self.lblExp.draw()
		self.answer = '2'

		self.syncKey = False