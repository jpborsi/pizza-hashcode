'''
@author: john.borsi
'''

from pizza_hashcode.core.solution import Solution
from pizza_hashcode.algorithms.solver import Solver


class EmptySolution(Solver):
    
    def get_solution(self, problem):
        return Solution()