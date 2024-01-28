import numpy, datetime
import matplotlib.pyplot as plot
import matplotlib.dates as dates
import matplotlib.ticker as ticker

start_date = datetime.datetime(1998, 1, 1)

def make_label(value, pos):
	# 1년이란 걸 365*value 형식으로 백분율화 시킴
	time = start_date + datetime.timedelta(days = 365 * value)
	return time.strftime('%b %y') # 월, 년 형식으로 반환

ax = plot.axes()
ax.xaxis.set_major_formatter(ticker.FuncFormatter(make_label))

X = numpy.linspace(0, 1, 256)
plot.plot(X, numpy.exp(-10 * X), c = 'k')
plot.plot(X, numpy.exp(-5 * X), c = 'k', ls = '--')

labels = ax.get_xticklabels()
plot.setp(labels, rotation = 30.)

plot.show()
