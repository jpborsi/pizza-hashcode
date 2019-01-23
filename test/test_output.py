'''
@author: john.borsi
'''
import os

from pizza_hashcode.core.solution import Solution
from pizza_hashcode.core.cut import Cut

from filecmp import cmp
import tempfile

def test_output():
    with tempfile.NamedTemporaryFile() as f:
        empty_solution = Solution()
        empty_solution.output(f.name)
        assert cmp('test/empty.out', f.name)
    
    with tempfile.NamedTemporaryFile() as f:
        non_empty_solution = Solution()
        non_empty_solution.add_cut(Cut(0,1,1,2))
        non_empty_solution.output(f.name)
        assert cmp('test/non_empty.out', f.name)
    
    