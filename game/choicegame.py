from game.gamearea import GameArea
import pyglet
from utils import draw


class ChoiceGame(GameArea):

	def __init__(self, title, width, height, **kwargs):

		super().__init__(title, width, height, **kwargs)

		self.answer = 1
		self.negative = -10

		self.lblQuestion = pyglet.text.Label('This is a question', x = self.width//2, anchor_x='center', y = self.description.y - 50, font_size = 18)

		choice_y = self.lblQuestion.y - 30
		self.choice1 = Choice('Choice 1', 1, self.width//2 - 100, choice_y )
		self.choice2 = Choice('Choice 2', 2, self.width//2 - 100, choice_y - 60 )
		self.choice3 = Choice('Choice 3', 3, self.width//2 - 100, choice_y - 120 )
		self.choice4 = Choice('Choice 4', 4, self.width//2 - 100, choice_y - 180 )

		self.choices = [self.choice1, self.choice2, self.choice3, self.choice4]

		self.window.push_handlers(on_draw = self.template_on_draw)
		self.window.push_handlers(on_draw = self.on_draw, on_mouse_release = self.on_mouse_release)


	def template_on_draw(self):
		self.lblQuestion.draw()
		self.choice1.draw()
		self.choice2.draw()
		self.choice3.draw()
		self.choice4.draw()


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
			print(i.text)
			self.submit(i.value)
			break


	def submit(self, ans):
		if ans == self.answer:
			self.updateScore(self.positive)
		else:
			self.updateScore(self.negative)
		self.addNew()


	def addNew(self):
		pass


	def on_draw(self):
		self.window.clear()



class Choice():
	'''
	Class to represent an option in the choice-type game
	'''
	w = 200
	h = 50
	def_color = [250, 250, 0]

	def __init__(self, text, value, x, y, color=[]):
		self.text = text
		self.value = value
		self.x = x
		self.y = y
		if len(color) == 0:
			self.color = self.def_color
		else:
			self.color = color


	def draw(self):
		self.figure = draw.rectangle(self.x, self.y, self.w, self.h, filled=True, color=self.color)
		self.figure.draw()