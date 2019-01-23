'''
Created on Jan 23, 2019

@author: john.borsi
'''

class Solution(object):

    def __init__(self):
        self.cuts = set()
        self.cells = set()
        
    def __eq__(self, other):
        return self.cuts == other.cuts
    
    def __contains__(self, cell):
        return cell in self.cells
        
    def output(self, filename):
        with open(filename, 'w+') as f:
            f.write('{}\n'.format(len(self.cuts)))
            for c in self.cuts:
                f.write('{} {} {} {}\n'.format(c.r1, c.c1, c.r2, c.c2))
    
    def add_cut(self, cut):
        self.cuts.add(cut)
        self.cells.update(cut.cells())
        
    def num_cuts(self):
        return len(self.cuts)
    
    def validate(self, cut):
        for cell in cut.cells():
            if cell in self.cells:
                return False
        return True