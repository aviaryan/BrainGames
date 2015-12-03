import pyglet


def square(x, y, length):
	return rectangle(x, y, length, length)


def rectangle(x, y, length, breadth):
	verts = [x, y,
			x+length, y,
			x+length, y-breadth,
			x, y-breadth]

	shape = pyglet.graphics.vertex_list(4, ('v2i', verts))

	pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)
	pyglet.gl.glColor3f(1,1,0)

	shape.draw(pyglet.gl.GL_LINE_LOOP)

	return shape