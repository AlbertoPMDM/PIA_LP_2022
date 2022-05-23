import numpy as np
from src.python.utils.utils import timing
from src.python.msws32.msws32 import msws32
import src.python.xorshift256 as xs

@timing
def f2(n):
    xs.rnd(0,1,np.zeros(n))

@timing
def f1(n):
    [i for i in msws32._rand32(0,1,n)]

f2(1000000)
f1(1000000)
