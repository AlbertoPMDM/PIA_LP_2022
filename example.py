import numpy as np
import matplotlib.pyplot as plt

from src.python.msws32.msws32 import msws32
import src.python.xorshift256 as xs
import src.python.faverage as fv

ax = -0.5
bx = 0.5
ay = -2
by = 2
n = 1000

def f(x, y):
    if (50/6)*x**2 + (1/2)*y**2 <= 2:
        return 1
    else:
        return 0

areas = []
n_areas = 1000

v_f = np.vectorize(f)
for _ in range(n_areas):
    areas.append(fv.faverage(ax+ay, bx+by, v_f( xs.rnd(ax,bx,np.zeros(n)), xs.rnd(ay,by,np.zeros(n)) )))

print(np.average(areas))

plt.title('Distribution of Areas Calculated')
plt.hist(areas, bins = 30, ec = 'black')
plt.xlabel('Areas')
plt.ylabel('Freq')
plt.show()