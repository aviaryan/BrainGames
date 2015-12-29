from game.gamearea import GameArea
from game.quesgame import QuesGame
from utils.draw import RectangularButton
import pyglet


class CellGame(QuesGame, GameArea):

	def __init__(self, title, width, height, **kwargs):

		GameArea.__init__(self, title, width, height, **kwargs)
		QuesGame.__init__(self, 10)

		self.choices = []
		self.curans = []
		self.window.push_handlers(on_draw = self.template_on_draw)
		self.window.push_handlers(on_draw = self.on_draw, on_mouse_release = self.on_mouse_release)

		self.addNew()
		self.beginPlay(autotime = False)


	def template_on_draw(self):
		pass


	def genTiles(self, n, m):
		'''
		generates the tiles on the screen
		n = rows
		m = columns
		'''
		cutoff_w = 70
		GAP = 3
		if n > 5 or m > 5:
			GAP = 2
		for i in self.choices:
			i.delete()
		self.choices = []

		xs = 140
		ys = self.description.y - 30
		m_gap = GAP
		n_gap = GAP
		m_w = ( self.width - xs*2 - (m-1)*m_gap ) // m
		if m_w > cutoff_w:
			xs += ((m_w - cutoff_w) * m)//2
			m_w = cutoff_w
		Cell._w = m_w
		k = 0
		for i in range(n):
			for j in range(m):
				self.choices += [ Cell('', k, xs + j*(m_w+m_gap), ys - i*(m_w+n_gap)) ]
				k += 1


	def on_mouse_release(self, x, y, button, modifiers):
		if self.syncKey:
			return
		if button != pyglet.window.mouse.LEFT:
			return
		for i in self.choices:
			if x < i.x or x > (i.x + i.w):
				continue
			if y > i.y or y < (i.y - i.h):
				continue
			self.curans += [i.value]
			self.check_answer()
			break


	def check_answer(self):
		print('hola')
		pass


	def addNew(self):
		self.genTiles(3,3)


	def on_draw(self):
		self.window.clear()
		for _ in self.choices:
			_.draw()


class Cell(RectangularButton):
	'''
	Represents a cell (tile)
	'''
	_w = 50
	_color = [255,255,255]
	_textcolor = [0,0,0,125]

	def __init__(self, text, value, x, y):
		super().__init__(text, value, x, y, w = self._w, h = self._w, color = self._color, textcolor = self._textcolor)