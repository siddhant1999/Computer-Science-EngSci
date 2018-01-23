class stackLib():
    
    def __init__(self):
        self.lis=[]
    def push(self, a):
        self.lis += [a]
    def pop(self):
        self.lis=self.lis[:-1]



x=stackLib()
x.push(1);
x.push(2);
x.push(3);
x.push(4);
x.pop();
x.pop();
#print x.lis

