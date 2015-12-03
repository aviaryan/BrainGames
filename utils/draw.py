import pyglet
from pyglet.gl import *


class Figure():
	'''
	figure class
	'''
	def __init__(self, figure, mode):
		self.figure = figure
		self.drawmode = mode

	def draw(self):
		'''
		Draw the figure on the window
		'''
		self.figure.draw(self.drawmode)



def square(x, y, length, **kwargs):
	'''
	returns a square figure
	'''
	return rectangle(x, y, length, length, **kwargs)


def rectangle(x, y, length, breadth, filled=False, color=[]):
	'''
	returns a rectangle figure
	'''
	verts = [x, y,
			x+length, y,
			x+length, y-breadth,
			x, y-breadth]

	shape = pyglet.graphics.vertex_list(4, ('v2i', verts))

	# pyglet.gl.glClearColor(0, 0.3, 0.5, 0)
	pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)
	if len(color) == 0:
		color = [255, 255, 0]
	pyglet.gl.glColor3f( color[0]/255.0 , color[1]/255.0 , color[2]/255.0 )

	# glPushMatrix()
	# glTranslatef(x, y, 0)
	# shape.draw(pyglet.gl.GL_LINE_LOOP)
	# glPopMatrix()

	return Figure(shape, GL_QUADS if filled else GL_LINE_LOOP)