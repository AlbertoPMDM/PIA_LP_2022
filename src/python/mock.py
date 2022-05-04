
from re import X


w = 0
x = 0
s = 0x100000000
s = 0xb5ad4eceda1ce2a9
 #64bit number relatively prime to 2^64
for i in range(100000):
    x*=x
    w+=s
    x+=w
    x = (x>>32 | x<<32) & 0xFFFFFFFF
    print(x/4294967296)
    # from interpolating 0,0 and 2^32, 1