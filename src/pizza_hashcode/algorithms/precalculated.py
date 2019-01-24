'''
@author: john.borsi
'''

from pizza_hashcode.core.cut import Cut
from pizza_hashcode.core.solution import Solution
from pizza_hashcode.algorithms.solver import Solver


class PrecalculatedSolution(Solver):

    def __init__(self, filename):
        self.solution = Solution()
        with open(filename) as f:
            first_line = True
            for line in f:
                if first_line:
                    first_line = False
                    self.expected_cuts = int(line.strip('\n'))
                    continue
                
                self.solution.add_cut(Cut(*[int(x) for x in line.strip('\n').split(' ')]))
        
        assert self.expected_cuts == self.solution.num_cuts()
    
    def get_solution(self, problem):
        return self.solution