import pyglet
from pyglet.gl import *
from math import *


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


def _setColor(color=[]):
	# pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)
	if len(color) == 0:
		color = [255, 255, 0]
	pyglet.gl.glColor3f( color[0]/255.0 , color[1]/255.0 , color[2]/255.0 )


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
	_setColor(color)
	return Figure(shape, GL_QUADS if filled else GL_LINE_LOOP)


def circle(xp, yp, radius, filled=False, color=[], numPoints=70):
	'''
	returns a circle figure
	'''
	verts = []
	xp += radius
	yp -= radius
	for i in range(numPoints):
		angle = radians(float(i)/numPoints * 360.0)
		x = radius*cos(angle) + xp
		y = radius*sin(angle) + yp
		verts += [x,y]
	circle = pyglet.graphics.vertex_list(numPoints, ('v2f', verts))
	_setColor(color)
	return Figure(circle, GL_POLYGON if filled else GL_LINE_LOOP)


def hexagon(xp, yp, radius, filled=False, color=[]):
	'''
	returns a hexagon figure
	'''
	return circle(xp, yp, radius, filled, color, numPoints=6)


def triangle(x, y, length, filled=False, color=[]):
	'''
	returns a triangle figure
	'''
	verts = [x + length//2, y,
			x, y - length,
			x + length, y - length]
	shape = pyglet.graphics.vertex_list(3, ('v2i', verts))
	_setColor(color)
	return Figure(shape, GL_TRIANGLES)


def color2Array(rgb):
	'''
	Converts color to array
	'''
	if rgb[0:1] == '#':
		rgb = rgb[1:]
	r = int(rgb[0:2], 16)
	g = int(rgb[2:4], 16)
	b = int(rgb[4:], 16)
	return [r, g, b]