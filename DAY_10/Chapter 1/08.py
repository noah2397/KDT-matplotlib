import numpy
import matplotlib.pyplot as plot

data = numpy.loadtxt('sample.txt')

for column in data.T: # Transpose하면 행을 열로, 열을 행으로 바꿈
	plot.plot(data[:,0], column)
	#data[:,0]은 0,1,2,3,4,5,6을 뜻한다
	# column은 data의 세로줄을 뜻한다

plot.show()

