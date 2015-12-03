import pyglet
from utils import draw

class GameArea():
	'''
	GameArea class.. create a new game
	'''

	def __init__(self, title, width, height, description=''):
		'''
		Init Game Area class
		'''

		self.window = pyglet.window.Window(width, height)
		self.heading = pyglet.text.Label(title, font_size=30, x = width // 2, y = height - 50, anchor_x = 'center')

		self.description = pyglet.text.Label(description, x = 30, y = height - 90)
		self.descriptiontext = description

		self.score = pyglet.text.Label('0', font_size=20, font_name='Times New Roman', x = width - 50, y = self.heading.y)
		self.scorebox = draw.rectangle(width - 70, self.score.y + 40, 60, 50)


		@self.window.event
		def on_draw():
			self.window.clear()
			self.heading.draw()
			self.description.draw()
			self.score.draw()
			self.scorebox.draw(pyglet.gl.GL_LINE_LOOP)


	def show(self):
		'''
		Make the game window visible
		'''
		pyglet.app.run()


	def descStatus(self, show=True):
		'''
		Shows or hides the description
		'''
		if show:
			self.description.text = self.descriptiontext
		else:
			self.description.text = ''
		self.description.draw()



if __name__ == '__main__':
	newgame = GameArea('My Game', 500, 500)
	newgame.show()