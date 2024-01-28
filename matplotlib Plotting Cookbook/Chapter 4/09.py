import numpy
import matplotlib.patches as patches
import matplotlib.pyplot as plot

ax = plot.axes(polar = True) # 극좌표계로 설정

theta = numpy.linspace(0, 2 * numpy.pi, 8, endpoint = False)
radius = .25 + .75 * numpy.random.random(size = len(theta)) # 0~1사이의 랜덤값을 뽑음
points = list(zip(theta, radius)) # 포인트를 x,y의 리스트 형태로 묶음

plot.gca().add_patch(patches.Polygon(points, color = '.75')) # gca()를 사용하여 다각형 생성

plot.show()
