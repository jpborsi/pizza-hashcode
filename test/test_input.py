'''
@author: john.borsi
'''
from pizza_hashcode.core.problem import Problem

def test_input_files():
    problem_a = Problem('input/a_example.in')
    problem_b = Problem('input/b_small.in')
    problem_c = Problem('input/c_medium.in')
    problem_d = Problem('input/d_big.in')
    
    assert problem_a is not None
    assert problem_a.num_rows == 3
    assert problem_a.num_cols == 5
    assert problem_a.min_toppings == 1
    assert problem_a.max_size == 6
    
    assert problem_a.pizza == [[False,False,False,False,False],
                               [False,True ,True ,True ,False],
                               [False,False,False,False,False]]
    
    assert problem_b is not None
    assert problem_c is not None
    assert problem_d is not None