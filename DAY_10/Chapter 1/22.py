import numpy
import matplotlib.pyplot as plot

data = numpy.random.randn(100, 5)
 # 평균 0 , 표준편차 1을 따르는 정규분포의 "리스트의 리스트" 생성

plot.boxplot(data)# 리스트의 리스트도 입력받는다
plot.show()
