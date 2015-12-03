import pyglet


class GameArea():
	'''
	GameArea class.. create a new game
	'''

	def __init__(self, title, width, height):
		'''
		Init Game Area class
		'''

		self.window = pyglet.window.Window(width, height)
		self.heading = pyglet.text.Label(title, font_size=30, x = self.window.width // 2, y = self.window.height - 50, anchor_x = 'center')
		self.score = pyglet.text.Label('0', font_size=20, font_name='Times New Roman', x = self.window.width - 50, y = self.heading.y)

		@self.window.event
		def on_draw():
			self.window.clear()
			self.heading.draw()
			self.score.draw()


	def show(self):
		'''
		Make the game window visible
		'''
		pyglet.app.run()



if __name__ == '__main__':
	newgame = GameArea('My Game', 500, 500)
	newgame.show()