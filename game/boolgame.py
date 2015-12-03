from game import gamearea
# import pyglet
from pyglet.window import key


class BoolGame(gamearea.GameArea):

	def __init__(self, title, width, height, **kwargs):

		super().__init__(title, width, height, **kwargs)


		@self.window.event
		def on_key_press(symbol, modifiers):
			if symbol == key.LEFT:
				print('left arrow key')
				self.descStatus()
			elif symbol == key.RIGHT:
				print('Right arrow key')
				self.descStatus(False)