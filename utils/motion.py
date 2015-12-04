import pyglet
from pyglet import clock

def slide(obj, fx, fy, dx=0, dy=0):
	'''
	Slides an object
	'''

	sigx = sig(fx - obj.x)
	sigy = sig(fy - obj.y)

	print (sigx, sigy)

	while sig(fx - obj.x) == sigx and sig(fy - obj.y) == sigy:
		pyglet.clock.tick()
		obj.x = obj.x + sigx * dx
		obj.y = obj.y + sigy * dy
		print(obj.y)
		obj.draw()


def sig(n):
	return -1 if n < 0 else 1


def wait(ms):
	a = clock.get_fps()
	ct = 0
	loopcount = (ms / 1000.0) * a
	while ct < loopcount:
		clock.tick()
		ct+=1