import pyglet

from game import colormatch
from game import mathgame
from game import calcgame
from game import scrabble
from game import colormeaning
from features import settings, gameover
from utils.draw import rectangle, color2Array

# newgame = boolgame.BoolGame('My game', width=700, height=500, description='test this thing')
# newgame.show()
# newgame.start()

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
		'description': 'Match if the previos color is same as current color',
		'color': '#0B3526'
	},
	{
		'name': 'Color Meaning',
		'gameid': 'colormeaning',
		'func': colormeaning.ColorMeaningGame,
		'description': 'Check if the meaning on the left is same as color on the right',
		'color': '#0B3526'
	}
]

# cards with bg color = color game
# mid titl
# then description

class BrainGames():
	'''
	The Brain Games home page
	'''
	def __init__(self):

		width = 700
		height = 550

		self.window = pyglet.window.Window(width, height, caption = 'Brain Games')
		self.heading = pyglet.text.Label('Brain Games', font_size=30, x = width // 2, y = height - 60, anchor_x = 'center')

		self.card0 = Card(GAMES[0]['name'], 0, 30, self.heading.y - 40, GAMES[0]['color'], description = GAMES[0]['description'])
		self.card1 = Card(GAMES[1]['name'], 1, 10 + self.card0.w + 50, self.heading.y - 40, GAMES[1]['color'], description = GAMES[1]['description'])

		self.option = 'colormatch'
		self.clickables = [self.card0, self.card1]

		@self.window.event
		def on_draw():
			self.window.clear()
			self.heading.draw()
			self.card0.draw()
			self.card1.draw()


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
		pyglet.app.exit()



class Card():
	'''
	Card element used in BrainGames homepage
	'''
	w = 300
	h = 100
	header_size = 16

	def __init__(self, heading, value, x, y, color, description=''):
		self.value = value
		self.x = x
		self.y = y
		if str(type(color)).find('str') > -1:
			color = color2Array(color)
		self.color = color
		self.heading = pyglet.text.Label(heading, x = x + self.w // 2, y = y, anchor_x = 'center', anchor_y = 'top', font_size = self.header_size)
		self.description = pyglet.text.Label(description, x = x + 5, y = y - 50, width = self.w - 10, multiline = True)


	def draw(self):
		self.figure = rectangle(self.x, self.y, self.w, self.h, filled=True, color=self.color)
		self.figure.draw()
		self.heading.draw()
		self.description.draw()


if __name__ == '__main__':

	x = BrainGames()
	option = x.start()
	if option > -1:
		print(option)