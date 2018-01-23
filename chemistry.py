class atom:
        atomlist = []
        cnt = {}
        def __init__(self, at):
                self.atomlist.append(at)
                self.curatom = at;
                if at in self.cnt:
                        self.cnt[at] +=1
                else:
                        self.cnt[at] = 1

                
        def addBond(self,a,b):
                return 0;

        def genformula(self):
                stri= ""
                for i in sorted(self.cnt.keys()):
                        stri += str(i)
                        stri +=("_")
                        stri += str(self.cnt[i])
                        stri += ("_")
                return stri[:-1]

