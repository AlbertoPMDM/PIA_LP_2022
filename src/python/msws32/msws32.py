from ctypes import c_uint64

#TODO change from generators to filling premade ctypes arrays
class msws32:
    '''
    class for a middle square wayle sequence random number generator
    '''

    _SEED = 0xb5ad4eceda1ce2a9

    __slots__ = {
        'state'
    }

    def __init__(self) -> None:
        self.state = [0, 0]

    def _randint32(n:int, seed:int = _SEED) -> int:
        '''
        generator type function that returns n random uints between 0 and 2^32
        '''
        x=c_uint64(0)
        w=c_uint64(0)
        s=c_uint64(seed)
        for _ in range(n):
            x = c_uint64(x.value **2)
            w = c_uint64(w.value + s.value)
            x = c_uint64(x.value + w.value)
            yield (x.value >> 32 | x.value << 32) & 0xFFFFFFFF

    def randint32(self, n:int, state:list, seed:int = _SEED) -> int:
        '''
        generator type function that returns n random uints between 0 and 2^32
        '''
        x=c_uint64(state[0])
        w=c_uint64(state[1])
        s=c_uint64(seed)
        for _ in range(n-1):
            x = c_uint64(x.value)
            x = c_uint64(x.value **2)
            w = c_uint64(w.value + s.value)
            x = c_uint64(x.value + w.value)
            yield (x.value >> 32 | x.value << 32) & 0xFFFFFFFF
        x = c_uint64(x.value)
        x = c_uint64(x.value **2)
        w = c_uint64(w.value + s.value)
        x = c_uint64(x.value + w.value)
        state[0] = x.value
        state[1] = w.value
        yield (x.value >> 32 | x.value << 32) & 0xFFFFFFFF

    def _rand32(min:float, max:float, n:int, seed:int = _SEED) -> float:
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
            yield ((max-min)/(4294967295)) * ((x.value >> 32 | x.value << 32) & 0xFFFFFFFF) + min

    def rand32(self, min:float, max:float, n:int, state:list, seed:int = _SEED) -> int:
        '''
        generator type function that returns n random uints between 0 and 2^32
        '''
        x=c_uint64(state[0])
        w=c_uint64(state[1])
        s=c_uint64(seed)
        for _ in range(n-1):
            x = c_uint64(x.value)
            x = c_uint64(x.value **2)
            w = c_uint64(w.value + s.value)
            x = c_uint64(x.value + w.value)
            yield ((max-min)/(2**32)) * ((x.value >> 32 | x.value << 32) & 0xFFFFFFFF) + min
        x = c_uint64(x.value)
        x = c_uint64(x.value **2)
        w = c_uint64(w.value + s.value)
        x = c_uint64(x.value + w.value)
        state[0] = x.value
        state[1] = w.value
        yield ((max-min)/(2**32)) * ((x.value >> 32 | x.value << 32) & 0xFFFFFFFF) + min
    
if __name__=='__main__':
    rand = msws32()
    for i in msws32._randint32(10):
        print(i)
    # a = [i for i in msws32.randint32(1)]
    # print(a)