from game import gamearea

class SubjectiveGame(gamearea.GameArea):


	def __init__(self, title, width, height, **kwargs):

		self.gameStarted = False

		super().__init__(title, width, height, **kwargs)

		self.window.push_handlers(on_key_release = self.on_key_release, on_draw = self.on_draw)


	def on_key_release(self, symbol, modifiers):
		print(symbol)


	def on_draw(self):
		pass