from game import gamearea
from pyglet.window import key
from utils import draw
import pyglet


class SubjectiveGame(gamearea.GameArea):


	def __init__(self, title, width, height, **kwargs):

		super().__init__(title, width, height, **kwargs)

		self.cText = ''
		self.negative = 0

		self.answerBox = draw.rectangle(self.width//2 - 100, self.description.y - 200, 200, 50, filled=True, color = draw.color2Array('95a799'))
		self.lblAnswer = pyglet.text.Label('', x = self.width//2, anchor_x = 'center', y = self.description.y - 200 - 10, anchor_y = 'top', font_size = 20)

		self.window.push_handlers(on_draw = self.template_on_draw)
		self.window.push_handlers(on_text = self.on_text, on_text_motion = self.on_text_motion, on_draw = self.on_draw)


	def on_text(self, text):
		self.cText += text
		self.lblAnswer.text = self.cText


	def on_text_motion(self, motion):
		# used for backspace
		if motion == key.MOTION_BACKSPACE:
			self.cText = self.cText[:-1]
			self.lblAnswer.text = self.cText


	def template_on_draw(self):
		self.answerBox.draw()
		self.lblAnswer.draw()


	def on_draw(self):
		self.window.clear()


	def addNew(self):
		pass


	def submit(self):
		'''
		Check answer, update point and change question in case of correct
		'''
		if self.cText == self.answer:
			self.updateScore(self.positive)
			print('correct answer')
		else:
			self.updateScore(self.negative)
			print('wrong answer', self.answer)
		self.addNew()
		self.lblAnswer.text = ''
		self.cText = ''