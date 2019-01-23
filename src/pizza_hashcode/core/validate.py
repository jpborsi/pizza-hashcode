'''
@author: john.borsi
'''

def validate(problem, solution):
    cells = set()
    for cut in solution.cuts:
        if not check_cut(problem, cut):
            return False
        for row in cut.rows():
            for col in cut.cols():
                if (row,col) in cells:
                    return False
                cells.add((row,col))
    return True

def check_cut(problem, cut):
    if cut.r1 < 0 or cut.c1 < 0 or cut.r2 < 0 or cut.c2 < 0:
        return False
    
    if cut.r1 > problem.num_rows or cut.c1 > problem.num_cols \
            or cut.r2 > problem.num_rows or cut.c2 > problem.num_cols:
        return False
    
    if cut.size() > problem.max_size:
        return False
    
    min_c = min(cut.c1, cut.c2)
    max_c = max(cut.c1, cut.c2)
    min_r = min(cut.r1, cut.r2)
    max_r = max(cut.r1, cut.r2)
    num_tomatoes = sum([sum(x[min_c:max_c+1]) for x in problem.pizza[min_r:max_r+1]])
    
    if num_tomatoes < problem.min_toppings or (cut.size() - num_tomatoes) < problem.min_toppings:
        return False
    return True