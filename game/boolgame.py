from game import gamearea
from utils import draw
from pyglet.window import key


class BoolGame(gamearea.GameArea):
	'''
	Boolean game which have option like Yes No
	'''

	def __init__(self, title, width, height, **kwargs):

		self.gameStarted = False

		super().__init__(title, width, height, **kwargs)

		self.window.push_handlers(on_draw = self.on_draw)
		

		@self.window.event
		def on_key_press(symbol, modifiers):
			if not self.gameStarted:
				self.descStatus(False)
				self.gameStarted = True
				self.beginPlay()
				self.addNew()
				return
			if self.syncKey:
				return
			if symbol == key.LEFT:
				self.submit(False)
			elif symbol == key.RIGHT:
				self.submit(True)


	def on_draw(self):
		pass


	def submit(self, ans):
		'''
		Checks the user's answer and then updates the game
		'''
		if (ans == self.answer):
			print('correct')
			self.updateScore(self.positive)
		else:
			print('incorrect')
			self.updateScore(self.negative)
		self.addNew()
		return


	def addNew(self):
		pass