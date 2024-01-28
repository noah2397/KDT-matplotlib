import numpy
import matplotlib.path as mpath # path를 추가로 import 함
from matplotlib import pyplot as plot

shape_description = [
	( 1.,  2., mpath.Path.MOVETO), # 처음 위치는 Moveto로 생성
	( 1.,  1., mpath.Path.LINETO), # 그 다음부터는 좌표계를 활용하여 이동함(Lineto)
	( 2.,  1., mpath.Path.LINETO),
	( 2., -1., mpath.Path.LINETO),
	( 1., -1., mpath.Path.LINETO),
  ( 1., -2., mpath.Path.LINETO),
	(-1., -2., mpath.Path.LINETO),
	(-1., -1., mpath.Path.LINETO),
	(-2., -1., mpath.Path.LINETO),
	(-2.,  1., mpath.Path.LINETO),
	(-1.,  1., mpath.Path.LINETO),
	(-1.,  2., mpath.Path.LINETO),
	( 0.,  0., mpath.Path.CLOSEPOLY), # 마지막은 Closepoly로 잇는다
]
# 종료점->.   |2   . <- 시작점
#            |
#   .   .    |1   .    .
#------------|--------------
#  -2   -1   |    1    2
#   .   .    |-1       .
#            |
#        .   |-2  . # 다음과 같이 점을 찍었다


u, v, codes = zip(*shape_description) # 해당 정보를 좌표 리스트와 명령 리스트에 저장
# Path객체의 생성자는 좌표 리스트와 명령 리스트를 입력으로 취함
# -> 좌표는 asarray를 사용하여 배열로 만들고, 명령어와 조합하여 Path객체 생성
my_marker = mpath.Path(numpy.asarray((u, v)).T, codes)

data = numpy.random.rand(8, 8)
plot.scatter(data[:,0], data[:, 1], c = '.75', marker = my_marker, s = 64)
plot.show()
