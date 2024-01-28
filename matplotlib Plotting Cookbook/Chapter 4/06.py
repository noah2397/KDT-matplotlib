import numpy
import matplotlib.pyplot as plot

X = numpy.linspace(1, 10, 1024)

# 해당 그래프의 y축 스케일을 log로 설정하여 넓은 폭을 볼 수 있게 함3
# base를 추가하여 로그 값 설정
plot.yscale('log', base=2)

# 범주를 라텍스 언어로 작성하였다
plot.plot(X, X, c = 'k', lw = 2., label = r'$f(x)=x$')
plot.plot(X, 10 ** X, c = '.75', ls = '--', lw = 2., label = r'$f(x)=e^x$')
plot.plot(X, numpy.log(X), c = '.75', lw = 2., label = r'$f(x)=\log(x)$')

plot.legend()
plot.show()
