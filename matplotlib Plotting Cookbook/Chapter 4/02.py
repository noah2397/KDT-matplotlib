import numpy
from matplotlib import pyplot as plot

def get_radius(T, params): # 도형을 만들어주는 함수
	m, n_1, n_2, n_3 = params # 언패킹하주기
	U = (m * T) / 4 # 도형 생성과정
	return (numpy.fabs(numpy.cos(U)) ** n_2 + numpy.fabs(numpy.sin(U)) ** n_3) ** (-1. / n_1)

grid_size = (3, 4)
T = numpy.linspace(0, 2 * numpy.pi, 1024)

for i in range(grid_size[0]): # 3
	for j in range(grid_size[1]): # 4
		# 4개짜리 1~20 사이의 숫자들을 리스트 형태로 생성
		params = numpy.random.random_integers(1, 20, size = 4)
		R = get_radius(T, params) # 반지름을 구해줌

		# 해당 위치에 하나하나씩 그림을 생성(rowspan, colspan을 둘 다 1로 설정)
		axes = plot.subplot2grid(grid_size, (i, j), rowspan=1, colspan=1)
		axes.get_xaxis().set_visible(False) # 축은 안보이게 설정
		axes.get_yaxis().set_visible(False)
		plot.plot(R * numpy.cos(T), R * numpy.sin(T), c = 'k')

		plot.title('%d, %d, %d, %d' % tuple(params), fontsize = 'small')

plot.tight_layout() # 서로 약간씩 떨어지게 설정
plot.show()
