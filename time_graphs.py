import numpy as np
import matplotlib.pyplot as plt

from src.python.utils.utils import timingTime
from src.python.msws32.msws32 import msws32
import src.python.xorshift256 as xs

@timingTime
def f2(n):
    xs.rnd(0,1,np.zeros(n))

@timingTime
def f1(n):
    [i for i in msws32._rand32(0,1,n)]

#### evaluating the time each fn takes for certain number of array elements
times = np.arange(0, 100000000, 10000000)
f1times = [f1(i) for i in times]
f2times = [f2(i) for i in times]

#### making the graphs for time taken per increase in array size
plt.title('Array size against time')
plt.plot(times, f2times, '-o', color = 'blue')
plt.ylabel('Time (s)')
plt.xlabel('Array Size')
plt.savefig('fortranTimes.png')

plt.title('Array size against time')
plt.plot(times, f1times, '-o', color = 'orange')
plt.ylabel('Time (s)')
plt.xlabel('Array Size')
plt.savefig('pythonTimes.png')
