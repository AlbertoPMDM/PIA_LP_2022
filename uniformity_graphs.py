import numpy as np
import matplotlib.pyplot as plt
from pyparsing import col

from src.python.msws32.msws32 import msws32
import src.python.xorshift256 as xs

def f1(n):
    return [i for i in msws32._rand32(0,1,n)]
def f2(n):
   return xs.rnd(0,1,np.zeros(n))


#### evaluating the time each fn takes for certain number of array elements
n = 10000000
f1samples = f1(n)
f2samples = f2(n)

#### making the graphs for time taken per increase in array size
plt.title('Frequency of numbers from 0 to 1 from 10000000 samples')
plt.hist(f1samples, bins = 30, ec = 'black', color='orange')
plt.ylabel('Freq')
plt.xlabel('Number')
plt.savefig('pythonSamplesHigh.png')
plt.cla()

plt.title('Frequency of numbers from 0 to 1 from 10000000 samples')
plt.hist(f2samples, bins = 30, ec = 'black', color='blue')
plt.ylabel('Freq')
plt.xlabel('Number')
plt.savefig('fortranSamplesHigh.png')
plt.cla()

#### evaluating the time each fn takes for certain number of array elements
n = 1000
f1samples = f1(n)
f2samples = f2(n)

#### making the graphs for time taken per increase in array size
plt.title('Frequency of numbers from 0 to 1 from 1000 samples')
plt.hist(f1samples, bins = 30, ec = 'black', color='orange')
plt.ylabel('Freq')
plt.xlabel('Number')
plt.savefig('pythonSamplesLow.png')
plt.cla()

plt.title('Frequency of numbers from 0 to 1 from 1000 samples')
plt.hist(f2samples, bins = 30, ec = 'black', color='blue')
plt.ylabel('Freq')
plt.xlabel('Number')
plt.savefig('fortranSamplesLow.png')