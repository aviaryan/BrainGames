from game import gamearea
from utils import draw, motion
# import pyglet
from pyglet.window import key


class BoolGame(gamearea.GameArea):
	'''
	Boolean game which have option like Yes No
	'''

	def __init__(self, title, width, height, **kwargs):

		self.gameStarted = False

		super().__init__(title, width, height, **kwargs)

		@self.window.event
		def on_draw():
			self.window.clear()
			for obj in self.components:
				obj.draw()

		@self.window.event
		def on_key_press(symbol, modifiers):
			if self.syncKey:
				return
			if symbol == key.LEFT:
				print('left arrow key')
				if not self.gameStarted:
					self.descStatus(False)
					self.gameStarted = True
					self.addNew()
				else:
					self.submit(False)
			elif symbol == key.RIGHT:
				print('Right arrow key')
				if not self.gameStarted:
					self.descStatus(False)
					self.gameStarted = True
					self.addNew()
				else:
					self.submit(True)


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


	def addNew(self):
		pass


	def start(self):
		self.show()
		self.gameStarted = False
		while not self.gameStarted:
			pass
		self.addNew()