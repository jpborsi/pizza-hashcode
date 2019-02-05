'''
@author: aaron.kub
'''
from pizza_hashcode.algorithms.akub.util import *


class ProblemParameters:

    def __init__(self, n_row, n_col, min_t, max_s, dense_topping=None):
        self.n_row = n_row
        self.n_col = n_col
        self.min_t = min_t
        self.max_s = max_s
        self.dense_topping = dense_topping  # most prevalent topping on the pizza


# Search algorithm class structure taken from Russel and Norvig's "Artificial Intelligence - A Modern Approach"
class PizzaProblem:

    def __init__(self, initial, goal, parameters):
        self.initial = initial
        self.goal = goal
        self.parameters = parameters
        self.n_cells = self.parameters.n_row * self.parameters.n_col

    def actions(self, state):
        return find_valid_slices(next_available_cell(state), state, self.parameters)

    def result(self, state, action):
        return get_remaining_pizza(state, action)

    def value(self, state):
        return get_number_of_cells_removed(state)

    def goal_test(self, state):
        return get_number_of_cells_removed(state) == self.n_cells

    def h(self, node):
        return self.n_cells - get_number_of_cells_removed(node.state)


class Node:

    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def expand(self, problem):
        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        next_state = problem.result(self.state, action)
        next_node = Node(next_state, self, action)
        return next_node

    def solution(self):
        return [node.action for node in self.path()[1:]]

    def path(self):
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state
