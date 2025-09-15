# Шаг 1
def inverse_list(lst: list) -> list:
    return lst[::-1]

# Шаг 2
def square_elements(lst : list[int]) -> list[int]:
    return [x**2 for x in lst]

# Шаг 3
def equal_lists(*lists) -> bool:
    res = True
    for l in lists:
        if l != lists[0]:
            res = False
            break
    return res

# Шаг 4
