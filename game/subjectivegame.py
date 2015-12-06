from game import gamearea
from pyglet.window import key


class SubjectiveGame(gamearea.GameArea):


	def __init__(self, title, width, height, **kwargs):

		self.gameStarted = False
		self.cText = ''

		super().__init__(title, width, height, **kwargs)

		self.window.push_handlers(on_text = self.on_text, on_text_motion = self.on_text_motion, on_draw = self.on_draw)


	def on_text(self, text):
		self.cText += text
		print(self.cText)


	def on_text_motion(self, motion):
		if motion == key.MOTION_BACKSPACE:
			self.cText = self.cText[:-1]


	def on_draw(self):
		pass