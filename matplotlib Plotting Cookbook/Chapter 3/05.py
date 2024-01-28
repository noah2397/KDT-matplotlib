import matplotlib.pyplot as plot

align_list = ('center', 'left', 'right')

ax1 = plot.axes()
ax1.axes.get_xaxis().set_visible(False)
ax1.axes.get_yaxis().set_visible(False)

for i, align in enumerate(align_list):
	# ha(horizontal alignment)에 매개변수 값을 바꿔가며 실행
	plot.text(0, i, 'align=\'%s\'' % align, ha = align)

# x축에 수직인 직선 그리기
plot.plot([0, 0], [-1, len(align_list)], c = '#808080', ls = '--')
plot.scatter([0] * len(align_list), range(len(align_list)))

plot.show()
