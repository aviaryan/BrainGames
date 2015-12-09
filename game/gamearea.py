import pyglet
from utils import draw, motion
from sys import exit



class GameArea():
	'''
	GameArea class.. create a new game
	'''

	def __init__(self, title, width, height, description='', color=''):
		'''
		Init Game Area class
		'''

		self.score = 0
		self.positive = 10
		self.negative = -20
		self.syncKey = False
		self.gameTime = 10
		self.timeLeft = 0
		self.gameid = 'gamearea'

		pyglet.clock.set_fps_limit(20)

		self.components = []
		self.window = pyglet.window.Window(width, height, caption = title)
		self.width = width
		self.height = height
		self.heading = pyglet.text.Label(title, font_size=30, x = width // 2, y = height - 60, anchor_x = 'center')

		self.description = pyglet.text.Label(description, font_size=12, x = 30, y = self.heading.y - 50)
		self.descriptiontext = description

		self.lblTimeLeft = pyglet.text.Label(str(self.gameTime), font_size=18, x = 40, y = self.heading.y)
		self.lblScore = pyglet.text.HTMLLabel(self.lblScoreHTML(), x = width - 80, y = self.heading.y)

		self.soundCorrect = pyglet.media.load('resources/correct.wav', streaming=False)
		self.soundFail = pyglet.media.load('resources/fail.wav', streaming=False)

		if color:
			self.setBackgroundColor( color )

		@self.window.event
		def on_draw():
			# self.window.clear()
			self.heading.draw()
			self.description.draw()
			self.lblScore.draw()
			self.lblTimeLeft.draw()

		@self.window.event
		def on_close():
			self.window.set_visible(False)


	def start(self):
		'''
		Run the game
		'''
		self.show()
		return (self.gameid, self.score)


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
		if by == self.positive:
			self.soundCorrect.play()
		elif by == self.negative:
			self.soundFail.play()
		self.score += by
		self.lblScore.text = self.lblScoreHTML()


	def setBackgroundColor(self, color):
		if str(type(color)).find('str'):
			color = draw.color2Array(color)
		if len(color) == 3:
			color += [255]
		pyglet.gl.glClearColor( color[0] / 255.0 , color[1] / 255.0 , color[2] / 255.0 , color[3] / 255.0 )


	def lblScoreHTML(self):
		'''
		returns the HTML code for score label display
		'''
		return '<b><font size=+3 color=gray>' + str(self.score) + '</font></b>'


	def beginPlay(self):
		self.lblTimeLeft.text = str(self.gameTime)
		self.timeLeft = self.gameTime
		pyglet.clock.schedule_interval(self.updateTime, 1)


	def updateTime(self, dt):
		self.timeLeft -= 1
		self.lblTimeLeft.text = str(self.timeLeft)
		if self.timeLeft == 0:
			self.endGame(0)
			pyglet.clock.unschedule(self.updateTime)


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