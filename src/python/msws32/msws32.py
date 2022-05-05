from ctypes import c_uint64

class msws32:
    '''
    class for a middle square wayle sequence random number generator
    '''

    _SEED = 0xb5ad4eceda1ce2a9

    def randint32(n:int, seed:int = _SEED) -> int:
        '''
        generator type function that returns n random uints between 0 and 2^32
        '''
        x=c_uint64(0)
        w=c_uint64(0)
        s=c_uint64(seed)
        for _ in range(n):
            x = c_uint64(x.value)
            x = c_uint64(x.value **2)
            w = c_uint64(w.value + s.value)
            x = c_uint64(x.value + w.value)
            yield (x.value >> 32 | x.value << 32) & 0xFFFFFFFF

    def rand32(min:float, max:float, n:int, seed:int = _SEED) -> float:
        '''
        generator function that returns n random floats between min and max
        '''
        x=c_uint64(0)
        w=c_uint64(0)
        s=c_uint64(seed)
        for _ in range(n):
            x = c_uint64(x.value)
            x = c_uint64(x.value **2)
            w = c_uint64(w.value + s.value)
            x = c_uint64(x.value + w.value)
            yield ((max-min)/(2**32)) * ((x.value >> 32 | x.value << 32) & 0xFFFFFFFF) + min

if __name__=='__main__':
    for i in msws32.rand32(-1,1,10):
        print(i)