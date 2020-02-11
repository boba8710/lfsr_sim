#lfsr

class FlipFlop:
    def __init__(self, init_val):
        self.val=init_val
    def Clock(self,new_val):
        output = self.val
        self.val = new_val
        return output
        
class LFSR:
    def __init__(self,init_vector, taps_vector):
        self.flipflops=[]
        self.m=len(init_vector)
        for i in range(self.m):
            self.flipflops.append(FlipFlop(init_vector[i]))
        assert len(taps_vector)==self.m
        self.taps_vector=taps_vector
    def Clock(self):
        feedback_val = 0
        for i in range(self.m):
            if(self.taps_vector[i]==1):
                feedback_val^=self.flipflops[i].val
        retval = self.flipflops[self.m-1].Clock(self.flipflops[self.m-2].val)
        for i in range(self.m-2,0,-1):
            self.flipflops[i].Clock(self.flipflops[i-1].val)
        self.flipflops[0].Clock(feedback_val)
        return retval
        
test = LFSR([0,0,0,0,0,0,0,1],[0,0,0,0,0,0,1,1])
for i in range(8):
    test.Clock()
def randbyte(lfsr):
    out = ""
    for i in range(8):
        out+=str(lfsr.Clock())
    out=int(out,base=2)
    return out
for i in range(50):
    print(randbyte(test))

