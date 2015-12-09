import pyglet

from game import colormatch
from game import mathgame
from game import calcgame
from game import scrabble
from game import colormeaning
from features import settings, gameover
from utils.draw import rectangle, color2Array

# newgame = colormatch.ColorMatchGame()
# newgame = mathgame.MathGame()
# newgame = calcgame.CalcGame()
# # newgame = scrabble.Scrabble()
# # newgame = colormeaning.ColorMeaningGame()

# x = newgame.start()

# settings.saveScore(x[0], x[1])

# n = gameover.GameOver(x[0], x[1])
# x = n.start()

# print(x)

GAMES = [
	{
		'name': 'Color Match',
		'gameid': 'colormatch',
		'func': colormatch.ColorMatchGame,
		'desc': 'Match if the previos color is same as current color',
		'color': '#0B3526'
	},
	{
		'name': 'Color Meaning',
		'gameid': 'colormeaning',
		'func': colormeaning.ColorMeaningGame,
		'desc': 'Check if the meaning on the left is same as color on the right',
		'color': '#0B3526'
	},
	{
		'name': 'Math Game',
		'gameid': 'mathgame',
		'func': mathgame.MathGame,
		'desc': 'Solve expressions fastly',
		'color': '#004000'
	},
	{
		'name': 'Calc Game',
		'gameid': 'calcgame',
		'func': calcgame.CalcGame,
		'desc': 'solve equations and write answers',
		'color': '#400000'
	},
	{
		'name': 'Scrabble',
		'gameid': 'scrabble',
		'func': scrabble.Scrabble,
		'desc': 'Choose the correct option for the jumbled word',
		'color': '#004040'
	}
]

# cards with bg color = color game
# mid titl
# then desc

class BrainGames():
	'''
	The Brain Games home page
	'''
	def __init__(self):

		width = 700
		height = 550

		self.window = pyglet.window.Window(width, height, caption = 'Brain Games')
		self.heading = pyglet.text.Label('Brain Games', font_size=30, x = width // 2, y = height - 60, anchor_x = 'center')

		self.card0 = Card(GAMES[0]['name'], 0, 30, self.heading.y - 40, GAMES[0]['color'], desc = GAMES[0]['desc'])
		self.card1 = Card(GAMES[1]['name'], 1, 30 + self.card0.w + 40, self.card0.y, GAMES[1]['color'], desc = GAMES[1]['desc'])
		self.card2 = Card(GAMES[2]['name'], 2, 30, self.card0.y - self.card0.h - 20, GAMES[2]['color'], desc = GAMES[2]['desc'])
		self.card3 = Card(GAMES[3]['name'], 3, 30 + self.card2.w + 40, self.card2.y, GAMES[3]['color'], desc = GAMES[3]['desc'])
		self.card4 = Card(GAMES[4]['name'], 4, 30, self.card2.y - self.card2.h - 20, GAMES[4]['color'], desc = GAMES[4]['desc'])

		self.option = 'colormatch'
		self.clickables = [self.card0, self.card1, self.card2, self.card3, self.card4]

		@self.window.event
		def on_draw():
			self.window.clear()
			self.heading.draw()
			for i in self.clickables:
				i.draw()


		@self.window.event
		def on_mouse_release(x, y, button, modifiers):
			if button != pyglet.window.mouse.LEFT:
				return
			for i in self.clickables:
				if x < i.x or x > (i.x + i.w):
					continue
				if y > i.y or y < (i.y - i.h):
					continue
				self.click_event(i.value)
				break


		@self.window.event
		def on_close():
			self.selected = -1


	def start(self):
		pyglet.app.run()
		return self.selected


	def click_event(self, value):
		self.selected = value
		self.window.set_visible(False)
		pyglet.app.exit()



class Card():
	'''
	Card element used in BrainGames homepage
	'''
	w = 300
	h = 100
	header_size = 16

	def __init__(self, heading, value, x, y, color, desc=''):
		self.value = value
		self.x = x
		self.y = y
		if str(type(color)).find('str') > -1:
			color = color2Array(color)
		self.color = color
		self.heading = pyglet.text.Label(heading, x = x + self.w // 2, y = y - 10, anchor_x = 'center', anchor_y = 'top', font_size = self.header_size, font_name = 'Verdana')
		self.desc = pyglet.text.Label(desc, x = x + 10, y = self.heading.y - 50, width = self.w - 20, multiline = True)


	def draw(self):
		self.figure = rectangle(self.x, self.y, self.w, self.h, filled=True, color=self.color)
		self.figure.draw()
		self.heading.draw()
		self.desc.draw()


if __name__ == '__main__':

	while True:
		x = ''
		x = BrainGames()
		option = x.start()
		if option > -1:
			while True:
				newgame = ''
				newgame = GAMES[option]['func']()
				gameresult = newgame.start()
				settings.saveScore(gameresult[0], gameresult[1])
				n = ''
				n = gameover.GameOver(gameresult[0], gameresult[1])
				result = n.start()
				if result == 0:
					break
		else:
			break