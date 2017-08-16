import numpy as np
import matplotlib.pyplot as plt

NUM_POINTS = 10000
INSIDE_COLOR = [0.0,1.0,0.0] # green
OUTSIDE_COLOR = [1.0,0.0,0.0] # red

"""Approximate PI as described at https://en.wikipedia.org/wiki/Monte_Carlo_method"""
def approximate_pi():
	inside = 0
	points_inside_x = []
	points_inside_y = []
	points_outside_x = []
	points_outside_y = []
	for i in range(1,NUM_POINTS):
		vec = np.random.random_sample(2)
		magnitude = np.sqrt(vec.dot(vec))
		if(magnitude <= 1):
			inside += 1
			points_inside_x.append(vec[0])
			points_inside_y.append(vec[1])
		else:
			points_outside_x.append(vec[0])
			points_outside_y.append(vec[1])						

		if(i%100 == 0):
			plt.title("π≈%.5f, n=%d" % (inside/i*4,i))
			plt.scatter(points_inside_x,points_inside_y,c=INSIDE_COLOR)
			plt.scatter(points_outside_x,points_outside_y,c=OUTSIDE_COLOR)
			plt.pause(0.05)


if __name__ == "__main__":
	fig = plt.figure(0)
	fig.canvas.set_window_title('Approximation of Pi')
	plt.axis([0,1,0,1])
	plt.ion() # activate interactive plot
	t = np.linspace(0,np.pi/2,100)
	x = np.cos(t)
	y = np.sin(t)
	plt.plot(x,y) # curve marking the edge of the quarter circle
	approximate_pi()
	plt.ioff()
	plt.show()
