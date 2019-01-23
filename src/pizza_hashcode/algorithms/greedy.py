'''
@author: john.borsi
'''
from pizza_hashcode.core.solution import Solution
from pizza_hashcode.core.validate import check_cut

class GreedySolver(object):

    def get_solution(self, problem):
        solution = Solution()
        for cell in problem.cells():
            if cell in solution:
                continue
            max_size = 0
            max_cut = None
            for cut in problem.potential_cuts(cell):
                if cut.size() > max_size and check_cut(problem, cut) and solution.validate(cut):
                    max_size = cut.size()
                    max_cut = cut
            if max_cut is not None:
                solution.add_cut(max_cut)
        return solution