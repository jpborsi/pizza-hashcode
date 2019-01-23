'''
@author: john.borsi
'''

from pizza_hashcode.core.validate import validate
from pizza_hashcode.core.problem import Problem
from pizza_hashcode.core.solution import Solution
from pizza_hashcode.core.cut import Cut

problem = Problem('input/a_example.in')

def test_validate():
    solution = Solution()
    solution.add_cut(Cut(0,0,2,1))
    solution.add_cut(Cut(0,2,2,2))
    solution.add_cut(Cut(0,3,2,4))
    
    assert validate(problem, solution)
    
def test_no_mushrooms():
    solution = Solution()
    solution.add_cut(Cut(0,0,4,0))
    
    assert not validate(problem, solution)
    
    
def test_too_big():
    solution = Solution()
    solution.add_cut(Cut(0,0,2,4))
    
    assert not validate(problem, solution)
    
def test_out_of_range():
    solution0 = Solution()
    solution0.add_cut(Cut(-1,0,2,1))
    
    solution1 = Solution()
    solution1.add_cut(Cut(0,0,4,3))
    
    assert not validate(problem, solution0)
    assert not validate(problem, solution1)
    
def test_overlap():
    solution = Solution()
    solution.add_cut(Cut(0,0,2,1))
    solution.add_cut(Cut(0,0,1,1))
    
    assert not validate(problem, solution)