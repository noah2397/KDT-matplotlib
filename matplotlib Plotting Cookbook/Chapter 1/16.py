import matplotlib.pyplot as plot

women_pop = [5., 30., 45., 22.]
men_pop   = [5., 25., 50., 20.]

X = range(4)
plot.barh(X, women_pop, color = 'r')
plot.barh(X, [-value for value in men_pop], color = 'b')
# 한 쪽은 -(minus)를 주어서 양쪽이 되도록 설정
plot.show()
