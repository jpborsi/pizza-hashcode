from pizza_hashcode.algorithms.akub.classes import Node
from pizza_hashcode.core.cut import Cut
from pizza_hashcode.core.solution import Solution
from pizza_hashcode.algorithms.solver import Solver
from pizza_hashcode.algorithms.akub.util import *
from pizza_hashcode.algorithms.akub.classes import PizzaProblem, ProblemParameters


# Tree Search Algorithm taken from Russel and Norvig's "Artificial Intelligence - A Modern Approach" (AIMA) GitHub page
# Link: https://github.com/aimacode/aima-python
def _depth_first_tree_search(problem):
    frontier = [Node(problem.initial)]

    while frontier:
        node = frontier.pop()
        if problem.goal_test(node.state):
            return node
        frontier.extend(node.expand(problem))

    return None


class TreeSearchSolver(Solver):

    def get_solution(self, problem):

        goal = [[None for i in range(problem.num_cols)] for j in range(problem.num_rows)]
        solution = Solution()

        pizza = [list(r) for r in problem.pizza]
        parameters = ProblemParameters(problem.num_rows, problem.num_cols, problem.min_toppings, problem.max_size)
        parameters.dense_topping = get_dense_topping(pizza, parameters)

        goal_node = _depth_first_tree_search(PizzaProblem(pizza, goal, parameters))

        for cut in goal_node.solution():
            solution.add_cut(Cut(cut[0], cut[1], cut[2], cut[3]))

        return solution
