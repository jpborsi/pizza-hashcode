'''
@author: john.borsi
'''

def score(problem, solution):
    score = 0
    for cut in solution.cuts:
        score += cut.size()
    return score