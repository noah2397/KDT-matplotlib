import numpy
import matplotlib.pyplot as plot


def pdf(X, mu, sigma):
	a = 1. / (sigma * numpy.sqrt(2. * numpy.pi))
	b = -1. / (2. * sigma ** 2)
	return a * numpy.exp(b * (X - mu) ** 2)
	#정규분포식을 생성하고 배열을 반환

X = numpy.linspace(-6, 6, 1024) # -6부터 6까지 1024개의 간격 설정

for i in range(5):
    # sample의 표준정규분포 데이터 5개 생성
	samples = numpy.random.standard_normal(50)
	mu, sigma = numpy.mean(samples), numpy.std(samples)
	plot.plot(X, pdf(X, mu, sigma), color = '.75')

# 완벽한 정규분포식을 표본으로 삼ㅁ음
plot.plot(X, pdf(X, 0., 1.), color = 'k')

plot.show()
