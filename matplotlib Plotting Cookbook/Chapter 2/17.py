import numpy
import matplotlib.pyplot as plot

data, label_list = [], []
for line in open('iris.data.txt'):
	tokens = line.split(',')
	data.append([float(s) for s in tokens[:-1]]) # 꽃 종류 열을 제외한 나머지를 data에 저장
	label_list.append(tokens[-1]) # 꽃 종류를 저장

# data : 꽃 수치
# label_list : 꽃 종류
data_map = { label : [] for label in set(label_list) }
for point, label in zip(data, label_list):
	data_map[label].append(point) # 각각의 꽃 종류에 해당하는 수치를 집어넣음
 
marker_set = ['^', 'x', '.'] # 마커 설정

for marker, (label, subset) in zip(marker_set, data_map.items()):
	data = numpy.asarray(subset) # 꽃 수치 데이터를 2차원으로 배열화시킴
	# 모든 행의 첫번째, 두번째 열을 인자로 넣음
	plot.scatter(data[:,0], data[:,1], color = 'k', marker = marker)

plot.show()
