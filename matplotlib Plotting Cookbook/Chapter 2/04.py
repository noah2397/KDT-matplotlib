import numpy
import matplotlib.pyplot as plot

data = numpy.random.standard_normal((100, 2))

#edgecolor 파라미터는 점의 가장자리 컬러를 제어한다
plot.scatter(data[:,0], data[:,1], color = '1.0', edgecolor='0.0')
plot.show()
