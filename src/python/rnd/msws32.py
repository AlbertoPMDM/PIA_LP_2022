
class msws32:

    SEED = 0xb5ad4eceda1ce2a9

    def randint32(n:int) -> int:
        x=0 
        w=0 
        s=msws32.SEED
        for i in range(n):
            x*=x
            w+=s 
            x+=w
            yield (x >> 32 | x << 32) & 0xFFFFFFFF

    def rand(min:float, max:float, x:int) -> float:
        return ((max-min)/(4294967296)) * x + min

if __name__=='__main__':
    print([msws32.rand(1,2,i) for i in msws32.randint32(17)])