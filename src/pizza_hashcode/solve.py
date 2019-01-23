'''
@author: john.borsi
'''

import sys
import time

import pizza_hashcode.algorithms as algorithms

from pizza_hashcode.core.problem import Problem
from pizza_hashcode.core.validate import validate
from pizza_hashcode.core.score import score

def main():
    config = sys.argv[1]
    total_score = 0
    with open(config) as f:
        for line in f:
            print(line)
            problem_name, input_file, output_file, algorithm, args = line.strip('\n').split(',')
            algorithm_class = getattr(algorithms, algorithm)
            init_args = tuple([x for x in args.strip('()').split(';') if len(x) > 0])
            solver = algorithm_class(*init_args)
            problem = Problem(input_file)
            start = time.time()
            solution = solver.get_solution(problem)
            end = time.time()
            solution.output(output_file)
            is_validated = validate(problem, solution)
            solution_score = score(problem, solution)
            
            print('---Problem {}---\nSolver: {}\nValidated: {}\nScore: {}\nTime: {:.2f} seconds\n'.format(
                problem_name,
                solver,
                is_validated,
                solution_score,
                end-start
                ))
            total_score += solution_score
            
    print('Total Score: {}\nPercent of Optimal: {:.2f}\n'.format(total_score, 1.0*total_score/1050057))