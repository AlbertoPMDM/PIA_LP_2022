import numpy as np
import matplotlib.pyplot as plt

from src.python.msws32.msws32 import msws32
import src.python.xorshift256 as xs

a = np.zeros(100000)
areas = xs.rnd(0,1,a)
# rand = msws32()
# a = 0
# b = np.pi
# n = 1000
# xrand = [i for i in rand.rand32(a, b, n, rand.state)]

# def f(x):
#     return np.sin(x)

# integral = 0
# for i in xrand:
#     integral += f(i)

# answer = (b-a)/n*integral

# areas = []
# n_areas = 1000
# for _ in range(n_areas):
#     xrand = [i for i in rand.rand32(a, b, n, rand.state)]

#     integral = 0
#     for i in xrand:
#         integral += f(i)
#     answer = (b-a)/n*integral

#     areas.append(answer)
plt.title('Distribution of Areas Calculated')
plt.hist(areas, bins = 30, ec = 'black')
plt.xlabel('Areas')
plt.ylabel('Freq')
plt.show()