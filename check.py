import re
from matplotlib.pyplot import *
import math

f = open("data.txt", 'r')
data = str(f.read())
numbers = []
num = {}
maxlen = 0
for x in re.findall(r"\d+\.?\d*", data):
	tmp = str(int(x.replace('.', '')))
	if (tmp in numbers):
		continue
	numbers.append(tmp)
	maxlen = max(len(tmp), maxlen)
	for i in range(len(tmp)):
		if (not num.get(i)):
			num[i] = []
		num[i].append(tmp)

resx = []
resy1 = []
resy2 = []
figure()
for l in range(min(5,maxlen)):
	for i in range(9 * (10 ** l)):
		resx.append(i+10**l)
		resy1.append(math.log10(i + 10 ** l + 1) - math.log10(i + 10 ** l))
		resy2.append(0)
	for i in num[l]:
		resy2[int(i[0:l + 1]) - 10 ** l] += 1 / len(num[l])
	if (l == 1 or l == 0):
		subplot(2, 2, 1+l*2)
		bar(resx, resy1)
		subplot(2, 2, 2+l*2)
		bar(resx, resy2)
	res = 0
	ly1 = 0
	ly2 = 0
	for i in range(len(resx)):
		ly1 += resy1[i]** 2
		ly2 += resy2[i]** 2
	ly1 = math.sqrt(ly1)
	ly2 = math.sqrt(ly2)
	for i in range(len(resx)):
		res += (resy1[i]/ly1*resy2[i]/ly2)
	print(l+1,"位数样本个数：",len(num[l]),"  相符度：",res)
show()