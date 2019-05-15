import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import random



def animation_update(num):
	global point
	global res
	tmp = np.pi*2*random.random()
	res += np.sin(tmp)
	point.append(tmp)
	plt.subplot(1, 2, 1)
	plt.plot(tmp,np.sin(tmp),"o",color = "r")
	plt.subplot(1, 2, 2)
	plt.plot(num, res / len(point), "o", color="b")
	plt.pause(0.01)
	

if __name__ == "__main__":
	global point
	global res
	point = []
	res = 0
	sin_x = np.arange(0, np.pi*2,0.1)
	sin_y = np.sin(sin_x)
	sta_x = np.arange(1, 200, 1)
	sta_y = sta_x * 0
	fig = plt.subplots(2,2)
	plt.subplot(1,2,1)
	l1, = plt.plot(sin_x, sin_y)
	plt.subplot(1, 2, 2)
	plt.ylim(-1, 1)
	l2, = plt.plot(sta_x, sta_y)
	plt.pause(5)
	for i in range(1, 200):
		animation_update(i)
	plt.show()

