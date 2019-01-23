'''
@author: john.borsi
'''
from math import floor, sqrt

from pizza_hashcode.core.cut import Cut

class Problem(object):


    def __init__(self, filename):

        with open(filename) as f:
            r, c, l, h = [int(s) for s in f.readline().split(" ")]
            self.num_rows = r
            self.num_cols = c
            self.min_toppings = l
            self.max_size = h
            
            self.pizza = []
            for _ in range(self.num_rows):
                self.pizza.append([t=='M' for t in f.readline().strip('\n')])
    
    def cells(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                yield (row, col)
                
    def potential_cuts(self, cell):
        rects = set()
        for x in range(2,int(floor(sqrt(self.max_size)))+1):
            for y in range(1,int(floor(self.max_size/x))+1):
                rects.add((x,y))
                rects.add((y,x))
        cuts = set()
        for rect in rects:
            for row_offset in range(rect[0]):
                for col_offset in range(rect[1]):
                    cuts.add(Cut(cell[0]-row_offset, cell[1]-col_offset, cell[0]-row_offset+rect[0]-1, cell[1]-col_offset+rect[1]-1))
        return cuts