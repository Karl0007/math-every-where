import matplotlib.pyplot as plt
import numpy as np
import random

def update(s:list):
	x = [x + 1 for x in range(0, 9)]
	global arr
	plt.subplot(1, 4, 3)
	ran = random.random()
	res = 0
	while (ran >= s[res]):
		res += 1
	arr[res] += 1
	su = sum(arr)
	plt.plot(9, ran, "o", color="w")
	plt.plot(res+1,ran,"o",color ="w")
	plt.subplot(1, 4, 4)
	plt.cla()
	plt.ylim(0,1)
	plt.bar(x,[arr[i]/su for i in range(0,9)])
	plt.pause(0.01)
	

x = [x+1 for x in range(0,9)]
f = [0 for x in range(0,9)]
s = [0 for x in range(0,9)]
global arr
arr = [0 for x in range(0, 9)]

for i in range(1, 10):
	f[i-1] = np.log10(i + 1) - np.log10(i)
	s[i-1] = s[i - 2] + f[i-1]
al = [[s[j]-(0 if i==0 else s[i-1])  if j>=i else 0 for j in range(0,9)] for i in range(0,9)]
plt.subplot(1, 4, 1)
plt.title("Probability Density Function")
plt.ylim(0,1)
plt.bar(x,f)
plt.subplot(1, 4, 2)
plt.title("Cumulative Density Function")
plt.ylim(0, 1)
for i in range(0, 9):
	plt.bar(x, al[i])
plt.bar(x, f)
plt.subplot(1, 4, 3)
plt.ylim(0, 1)
for i in range(0, 9):
	plt.bar(x, [s[8 - i] if j >= 8 - i else 0 for j in range(0, 9)])
plt.pause(5)
for i in range(0, 200):
	update(s)

plt.show()