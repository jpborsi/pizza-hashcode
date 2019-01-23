'''
@author: john.borsi
'''
from pizza_hashcode.algorithms.empty_solution import EmptySolution
from pizza_hashcode.core.problem import Problem
from pizza_hashcode.core.solution import Solution

def test_empty():
    solver = EmptySolution()
    problem = Problem('input/a_example.in')
    solution = solver.get_solution(problem)
    
    assert solution == Solution()