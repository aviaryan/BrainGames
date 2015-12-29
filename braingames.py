import pyglet

from game.colormatch import ColorMatchGame
from game.mathgame import MathGame
from game.calcgame import CalcGame
from game.scrabble import Scrabble
from game.colormeaning import ColorMeaningGame
from game.dictionarygame import DictionaryGame
from features import settings, gameover
from utils.draw import rectangle, color2Array

from sys import exit
from game.cellgame import CellGame
x = CellGame('ADASDASDDS', 600, 500)
print( x.start() )
exit()

gms = [ColorMatchGame, ColorMeaningGame, MathGame, CalcGame, Scrabble, DictionaryGame]
GAMES = []
for i in gms:
	GAMES += [{
		'name': i.title,
		'gameid': i.gameid,
		'func': i,
		'desc': i.descriptiontext,
		'color': i.color
	}]


class BrainGames():
	'''
	The Brain Games home page
	'''
	def __init__(self):

		width = 700
		height = 550

		self.window = pyglet.window.Window(width, height, caption = 'Brain Games')
		self.heading = pyglet.text.Label('Brain Games', font_size=30, x = width // 2, y = height - 60, anchor_x = 'center')

		self.card0 = Card(GAMES[0]['name'], 0, 30, self.heading.y - 60, GAMES[0]['color'], desc = GAMES[0]['desc'])
		self.card1 = Card(GAMES[1]['name'], 1, 30 + self.card0.w + 40, self.card0.y, GAMES[1]['color'], desc = GAMES[1]['desc'])
		self.card2 = Card(GAMES[2]['name'], 2, 30, self.card0.y - self.card0.h - 20, GAMES[2]['color'], desc = GAMES[2]['desc'])
		self.card3 = Card(GAMES[3]['name'], 3, 30 + self.card2.w + 40, self.card2.y, GAMES[3]['color'], desc = GAMES[3]['desc'])
		self.card4 = Card(GAMES[4]['name'], 4, 30, self.card2.y - self.card2.h - 20, GAMES[4]['color'], desc = GAMES[4]['desc'])
		self.card5 = Card(GAMES[5]['name'], 5, 30 + self.card4.w + 40, self.card4.y, GAMES[5]['color'], desc = GAMES[5]['desc'])

		self.option = 'colormatch'
		self.clickables = [self.card0, self.card1, self.card2, self.card3, self.card4, self.card5]

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
		self.window.pop_handlers()
		self.window.close()
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


def getGame(gameid):
	'''
	Get the game from GAMES array searching through game id
	'''
	for i in GAMES:
		if i['gameid'] == gameid:
			return i


if __name__ == '__main__':

	while True:
		x = BrainGames()
		option = x.start()
		if option > -1:
			while True:
				newgame = GAMES[option]['func']()
				result = newgame.start()
				settings.saveScore(result['gameid'], result['score'])
				game = getGame(result['gameid'])
				n = gameover.GameOver( game['name'], result['score'], width = result['width'], height = result['height'], 
					highscore = settings.getHighScore(result['gameid']) )
				result = n.start()
				if result == 0:
					break
		else:
			break