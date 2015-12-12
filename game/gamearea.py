import pyglet
from utils import draw
from features import settings


class GameArea():
	'''
	GameArea class.. create a new game
	'''

	def __init__(self, title, width, height, description='', color=''):
		'''
		Init Game Area class
		'''

		# self.gameid = ''
		self.score = 0
		self.positive = 10
		self.negative = -20
		self.syncKey = False
		self.gameTime = 45
		# self.timeLeft self.quesLeft
		self.numQuestions = 10
		self.gameStatus = -1 # not started | started | over
		self._loadSetting( settings.loadSettings() )

		self.components = []
		self.window = pyglet.window.Window(width, height, caption = title)
		self.width = width
		self.height = height
		self.heading = pyglet.text.Label(title, font_size=30, x = width // 2, y = height - 60, anchor_x = 'center')

		self.description = pyglet.text.Label(description, font_size=12, x = 30, y = self.heading.y - 50, width = self.width - 60, multiline = True)
		self.descriptiontext = description

		self.lblTimeLeft = pyglet.text.Label(str(self.gameTime), font_size=18, x = 40, y = self.heading.y)
		self.lblScore = pyglet.text.HTMLLabel(self.lblScoreHTML(), x = width - 80, y = self.heading.y)

		self.soundCorrect = pyglet.media.load('resources/correct.wav', streaming=False)
		self.soundFail = pyglet.media.load('resources/fail.wav', streaming=False)

		if color:
			self.setBackgroundColor( color )

		@self.window.event
		def on_draw():
			self.heading.draw()
			self.description.draw()
			self.lblScore.draw()
			self.lblTimeLeft.draw()

		@self.window.event
		def on_close():
			self.cleanup(True)


	def start(self):
		'''
		Run the game
		'''
		self.show()
		return {
				'gameid': self.gameid,
				'score': self.score if self.gameStatus == 1 else '',
				'width': self.width,
				'height': self.height
			}


	def cleanup(self, advanced=True):
		if advanced:
			pyglet.clock.unschedule(self.updateTime)
		self.window.pop_handlers()
		self.window.close()
		pyglet.app.exit()


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
		self.bgColor = color[:]
		pyglet.gl.glClearColor( color[0] / 255.0 , color[1] / 255.0 , color[2] / 255.0 , color[3] / 255.0 )


	def lblScoreHTML(self):
		'''
		returns the HTML code for score label display
		'''
		return '<b><font size=+3 color=gray>' + str(self.score) + '</font></b>'


	def beginPlay(self, autotime = True):
		self.lblTimeLeft.text = str(self.gameTime)
		self.timeLeft = self.gameTime
		self.gameStatus = 0
		if self.timeLeft == 0:
			self.endTime()
		elif autotime:
			pyglet.clock.schedule_interval(self.updateTime, 1)


	def endTime(self):
		'''
		launched when time ends
		'''
		self.endGame()


	def updateTime(self, dt=1):
		'''
		runs sec after sec, updating timeLeft
		'''
		self.timeLeft -= 1
		self.lblTimeLeft.text = str(self.timeLeft)
		if self.timeLeft < 1:
			pyglet.clock.unschedule(self.updateTime)
			self.endTime()


	def loadGameSettings(self):
		'''
		load game specific settings from file
		'''
		config = settings.loadGameSettings(self.gameid)
		self._loadSetting(config)


	def _loadSetting(self, config):
		self.gameTime = config.get('gameTime', self.gameTime)
		self.positive = config.get('positive', self.positive)
		self.negative = config.get('negative', self.negative)
		self.numQuestions = config.get('numQuestions', self.numQuestions)


	def endGame(self):
		'''
		ends the game
		'''
		print('Game over')
		while self.syncKey:
			pass
		self.syncKey = True
		self.gameStatus = 1
		self.cleanup(False)


if __name__ == '__main__':
	newgame = GameArea('My Game', 500, 500)
	newgame.show()