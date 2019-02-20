'''
@author: aaron.kub
'''


def next_available_cell(pizza):
    for col in range(len(pizza[0])):
        for row in range(len(pizza)):
            if pizza[row][col] is not None:
                return row, col
    return None


def all_cells_taken(pizza):
    for temp_row in pizza:
        for topping in temp_row:
            if topping is not None:
                return False
    return True


def has_min_toppings(pizza_slice, min_toppings):
    n_mushrooms = 0
    n_tomatoes = 0
    for temp_row in pizza_slice:
        temp_mush_count = sum([t is True for t in temp_row])
        n_mushrooms += temp_mush_count
        n_tomatoes += (len(temp_row) - temp_mush_count)

    return n_mushrooms >= min_toppings and n_tomatoes >= min_toppings


def get_cell_count(coordinates):
    upper_row = coordinates[0]
    left_col = coordinates[1]
    lower_row = coordinates[2]
    right_col = coordinates[3]

    area = (lower_row - upper_row + 1) * (right_col - left_col + 1)
    return area


def get_slice_from_coordinates(coordinates, new_pizza):
    pizza_slice = []
    for i in range(coordinates[0], coordinates[2] + 1):
        pizza_slice.append(new_pizza[i][coordinates[1]:coordinates[3] + 1])
    return pizza_slice


def remove_slice(coordinates, new_pizza):
    for temp_row in range(coordinates[0], coordinates[2] + 1):
        for column in range(coordinates[1], coordinates[3] + 1):
            new_pizza[temp_row][column] = None


def all_cells_available(pizza_slice):
    for row in pizza_slice:
        if None in row:
            return False
    return True


def is_valid_slice(pizza, coordinates, min_toppings, max_size):
    pizza_slice = get_slice_from_coordinates(coordinates, pizza)
    cells_available = all_cells_available(pizza_slice)
    has_topping_requirement = has_min_toppings(pizza_slice, min_toppings)
    valid_cell_count = get_cell_count(coordinates) <= max_size
    return cells_available and has_topping_requirement and valid_cell_count


def get_next_available_cell(pizza):
    for row in range(len(pizza)):
        for column in range(len(pizza[row])):
            if pizza[row][column] is not None:
                return row, column
    return None


def get_dense_topping(pizza, parameters):
    n_cells = get_cell_count((0, 0, parameters.n_row - 1, parameters.n_col - 1))
    n_mushrooms = 0
    for row in pizza:
        n_mushrooms += sum([t is True for t in row])
    n_tomatoes = n_cells - n_mushrooms
    return True if n_mushrooms >= n_tomatoes else False


def get_proportion_with_dense_topping(coordinates, pizza_slice, dense_topping):
    n_cells = get_cell_count(coordinates)
    n_dense = 0
    for row in pizza_slice:
        n_dense += sum([t is dense_topping for t in row])
    return n_dense / n_cells


def pick_best_slice(coordinates, pizza, parameters):
    base_score = get_cell_count(coordinates)
    density = get_proportion_with_dense_topping(
        coordinates, get_slice_from_coordinates(coordinates, pizza), parameters.dense_topping
    )
    return base_score + density


def sort_by_best_slices(slices, pizza, parameters, reverse):
    slices.sort(key=lambda x: pick_best_slice(x, pizza, parameters), reverse=reverse)


def get_remaining_pizza(old_pizza, coordinates):
    temp_pizza = [list(s) for s in old_pizza]
    for temp_row in range(coordinates[0], coordinates[2] + 1):
        for column in range(coordinates[1], coordinates[3] + 1):
            temp_pizza[temp_row][column] = None
    return temp_pizza


def get_number_of_cells_removed(pizza):
    n_removed = 0
    for temp_row in pizza:
        n_removed += sum([t is None for t in temp_row])
    return n_removed


def find_valid_slices(starting_cell, pizza, parameters, reverse=False):

    valid_slices = []

    row_max = min(parameters.n_row, starting_cell[0] + parameters.max_s)
    col_max = min(parameters.n_col, starting_cell[1] + parameters.max_s)

    for r2 in range(starting_cell[0], row_max):
        for c2 in range(starting_cell[1], col_max):

            contender = (starting_cell[0], starting_cell[1], r2, c2)
            if is_valid_slice(pizza, contender, parameters.min_t, parameters.max_s):
                valid_slices.append(contender)

    sort_by_best_slices(valid_slices, pizza, parameters, reverse)

    return valid_slices
