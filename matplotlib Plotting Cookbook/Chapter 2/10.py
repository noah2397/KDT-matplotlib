import random
import matplotlib.cm as cm # 해당 컬러맵과
import matplotlib.colors as col # 컬러를 import 함
import matplotlib.pyplot as plot

values = [random.randint(0, 99) for i in range(50)]
values.sort()

# 값을 [0,99]에서 matplotlib.cm.binary 컬러맵의 컬러로 사상하기 위해
# cmap 컬러맵을 먼저 생성함
cmap = cm.ScalarMappable(col.Normalize(0, 99), cm.binary)

# .to_rgba함수 : 값 리스트를 컬러 리스트로 변환
# 그런 후의 pyplot.bar는 컬러맵을 지원하지 않지만, 복잡한 코드를 수반하지 않는 컬러맵을 이용하였다
plot.bar(range(len(values)), values, color = cmap.to_rgba(values))
plot.show()
