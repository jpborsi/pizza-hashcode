'''
@author: john.borsi
'''

from pizza_hashcode.algorithms.precalculated import PrecalculatedSolution
from pizza_hashcode.core.cut import Cut
from pizza_hashcode.core.problem import Problem
from pizza_hashcode.core.solution import Solution


def test_precalculated():
    solver = PrecalculatedSolution('precalculated/a.out')
    problem = Problem('input/a_example.in')
    solution = solver.get_solution(problem)
    
    expected_solution = Solution()
    expected_solution.add_cut(Cut(0,0,2,1))
    expected_solution.add_cut(Cut(0,2,2,2))
    expected_solution.add_cut(Cut(0,3,2,4))
    assert solution == expected_solution