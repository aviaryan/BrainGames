from game import colormatch
from game import mathgame


# newgame = boolgame.BoolGame('My game', width=700, height=500, description='test this thing')
# newgame.show()
# newgame.start()

# newgame = colormatch.ColorMatchGame(700, 500)
newgame = mathgame.MathGame(600, 500)


newgame.start()