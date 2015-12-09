import pyglet

class GameOver():

	def __init__(self, title, score):

		width = 600
		height = 500
		self.window = pyglet.window.Window(width, height, caption = title)
		self.heading = pyglet.text.Label(title, font_size=30, x = width // 2, y = height - 60, anchor_x = 'center')

		self.score = pyglet.text.Label(str(score), font_size=26, x = width // 2, y = self.heading.y - 100, anchor_x = 'center')


		@self.window.event
		def on_draw():
			self.window.clear()
			self.heading.draw()
			self.score.draw()

		@self.window.event
		def on_close():
			self.window.set_visible(False)


	def show(self):
		pyglet.app.run()
		return 0