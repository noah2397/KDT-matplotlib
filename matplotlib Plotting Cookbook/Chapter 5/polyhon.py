import numpy as np
import matplotlib.pyplot as plt

theta=np.linspace(0,2*np.pi,8)
points=np.vstack((np.cos(theta), np.sin(theta))).transpose()

plt.figure(figsize=(4.,4.))
plt.gca().add_patch(plt.Polygon(points, color='0.75')) # 다각형 그리기

plt.grid(True)
plt.axis('scaled') # 축의 비율 동일하게 유지

plt.savefig('polygon.png', dpi=128) # 512X512