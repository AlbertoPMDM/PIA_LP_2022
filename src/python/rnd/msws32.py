from ctypes import c_uint64

class msws32:

    SEED = 0xb5ad4eceda1ce2a9

    def randint32(n:int) -> int:
        x=c_uint64(0)
        w=c_uint64(0)
        s=c_uint64(msws32.SEED)
        for i in range(n):
            print(hex(x.value))
            x = c_uint64(x.value)
            x = c_uint64(x.value **2)
            w = c_uint64(w.value + s.value)
            x = c_uint64(x.value + w.value)
            yield (x.value >> 32 | x.value << 32) & 0xFFFFFFFF

    def rand(min:float, max:float, x:int) -> float:
        return ((max-min)/(4294967296)) * x + min

if __name__=='__main__':
    for i in msws32.randint32(5000):
        print(msws32.rand(1,2,i))