import numpy as np
import matplotlib.pyplot as plt

from src.python.msws32.msws32 import msws32
import src.python.xorshift256 as xs
import src.python.faverage as fv

a = 0
b = np.pi
n = 10000
xrand = xs.rnd(a,b,np.zeros(n))

def f(x):
    return np.sin(x)

areas = []
n_areas = 1000

v_f = np.vectorize(f)
for _ in range(n_areas):
    areas.append(fv.faverage(a, b, v_f(xs.rnd(a,b,np.zeros(n)))))

plt.title('Distribution of Areas Calculated')
plt.hist(areas, bins = 30, ec = 'black')
plt.xlabel('Areas')
plt.ylabel('Freq')