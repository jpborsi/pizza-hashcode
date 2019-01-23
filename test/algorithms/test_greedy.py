'''
@author: john.borsi
'''
from pizza_hashcode.algorithms.greedy import GreedySolver
from pizza_hashcode.core.problem import Problem
from pizza_hashcode.core.validate import validate

def test_greedy():
    solver = GreedySolver()
    problem = Problem('input/a_example.in')
    solution = solver.get_solution(problem)
    
    assert solution is not None
    assert validate(problem, solution)