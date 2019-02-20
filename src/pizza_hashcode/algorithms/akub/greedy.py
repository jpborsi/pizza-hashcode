'''
@author: aaron.kub
'''
from pizza_hashcode.core.cut import Cut
from pizza_hashcode.core.solution import Solution
from pizza_hashcode.algorithms.solver import Solver
from pizza_hashcode.algorithms.akub.util import *
from pizza_hashcode.algorithms.akub.classes import ProblemParameters


class GreedySolver2(Solver):

    def get_solution(self, problem):

        solution = Solution()
        pizza = [list(r) for r in problem.pizza]
        parameters = ProblemParameters(problem.num_rows, problem.num_cols, problem.min_toppings, problem.max_size)
        parameters.dense_topping = get_dense_topping(pizza, parameters)
        for cell in problem.cells():

            if cell in solution:
                continue

            valid_slices = find_valid_slices(cell, pizza, parameters, reverse=True)

            if len(valid_slices) > 0:

                cut = valid_slices[0]
                remove_slice(cut, pizza)
                solution.add_cut(Cut(cut[0], cut[1], cut[2], cut[3]))

        return solution
