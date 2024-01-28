import numpy
import matplotlib.pyplot as plot

# 2차원 형태의 분포 중심이 0,0을 따르는 x,y좌표값 생성
A = numpy.random.standard_normal((100, 2))
A += numpy.array((-1, -1)) # 각 요소에 값을 더함으로써
# 분포 중심은 (-1,-1)로 만들어줌
print(A)

B = numpy.random.standard_normal((100, 2))
B += numpy.array((1, 1)) # 분포 중심은 (1,1)

# A[:,0] : 전체행, 1번째 열
# A[:,1] : 전체행, 2번째 열
plot.scatter(A[:,0], A[:,1], color = '.25')
plot.scatter(B[:,0], B[:,1], color = '.75')

plot.show()
