'''
@author: john.borsi
'''

from pizza_hashcode.core.problem import Problem
from pizza_hashcode.core.solution import Solution
from pizza_hashcode.core.cut import Cut
from pizza_hashcode.core.score import score

def test_score():
    problem = Problem('input/a_example.in')
    solution0 = Solution()
    solution0.add_cut(Cut(0,0,2,1))
    solution0.add_cut(Cut(0,2,2,2))
    solution0.add_cut(Cut(0,3,2,4))
    
    assert score(problem, solution0) == 15