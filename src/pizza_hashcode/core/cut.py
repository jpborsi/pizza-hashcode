'''
@author: john.borsi
'''

class Cut(object):
    
    def __init__(self, r1, c1, r2, c2):
        self.r1 = min(r1, r2)
        self.c1 = min(c1, c2)
        self.r2 = max(r1, r2)
        self.c2 = max(c1, c2)
        
    def __eq__(self, other):
        return self.r1 == other.r1 and self.r2 == other.r2 and\
            self.c1 == other.c1 and self.c2 == other.c2
            
    def __hash__(self):
        return hash((self.r1, self.c1, self.r2, self.c2))
    
    def size(self):
        return (self.r2 - self.r1 + 1) * (self.c2 - self.c1 + 1)
    
    def rows(self):
        return range(self.r1, self.r2+1)
    
    def cols(self):
        return range(self.c1, self.c2+1)
    
    def cells(self):
        result = set()
        for row in self.rows():
            for col in self.cols():
                result.add((row,col))
        return result