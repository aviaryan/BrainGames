import pyglet
from utils import draw, motion
from sys import exit

class GameArea():
	'''
	GameArea class.. create a new game
	'''

	def __init__(self, title, width, height, description=''):
		'''
		Init Game Area class
		'''

		self.score = 0
		self.positive = 10
		self.negative = -20
		self.syncKey = False
		self.gameTime = 10

		pyglet.clock.set_fps_limit(10)

		self.components = []
		self.window = pyglet.window.Window(width, height)
		self.width = width
		self.height = height
		self.heading = pyglet.text.Label(title, font_size=30, x = width // 2, y = height - 60, anchor_x = 'center')

		self.description = pyglet.text.Label(description, font_size=12, x = 30, y = self.heading.y - 50)
		self.descriptiontext = description

		self.lblScore = pyglet.text.HTMLLabel(self.lblScoreHTML(), x = width - 80, y = self.heading.y)

		@self.window.event
		def on_draw():
			# self.window.clear()
			self.heading.draw()
			self.description.draw()
			self.lblScore.draw()

		@self.window.event
		def on_close():
			exit(0)


	def start(self):
		'''
		Run the game
		'''
		self.show()


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


	def updateScore(self, by):
		'''
		Updates the score
		'''
		#self.updateScoreFlyer(str(by))
		self.score += by
		self.lblScore.text = self.lblScoreHTML()
		self.lblScore.draw()


	def lblScoreHTML(self):
		'''
		returns the HTML code for score label display
		'''
		return '<b><font size=+3 color=gray>' + str(self.score) + '</font></b>'


	# def updateScoreFlyer(self, content):
	# 	'''
	# 	Shows the score flyer animation
	# 	'''
	# 	for i in self.components_temp:
	# 		i.delete()
	# 	self.components_temp = []
	# 	flyer = pyglet.text.Label(content, font_size=20, x = self.lblScore.x, y = self.lblScore.y - 200)
	# 	self.components_temp += [flyer]
	# 	flyer.draw()
	# 	Thread( motion.slide(flyer, flyer.x, flyer.y + 200, 0, 20) ).start()


	def endGame(self, dt):
		print('Game over')
		while self.syncKey:
			pass
		self.syncKey = True


if __name__ == '__main__':
	newgame = GameArea('My Game', 500, 500)
	newgame.show()