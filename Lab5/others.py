from typing import Any, Iterable, List, Tuple, Dict, Optional
import random
import itertools


# (Шаг 1)
def reverse_list(lst: List[Any]) -> List[Any]:
    return lst[::-1]


# (Шаг 2)
def modify_list_values(lst: List[Any], replacements: Dict[int, Any] = None,
                       replace_all: Any = None) -> List[Any]:
    if replace_all is not None:
        for i in range(len(lst)):
            lst[i] = replace_all
        return lst

    if replacements:
        for idx, val in replacements.items():
            if -len(lst) <= idx < len(lst):
                lst[idx] = val
    return lst

# (Шаг 3)
def are_all_lists_equal(*lists: List[Any]) -> bool:
    if len(lists) < 2:
        return True
    first = lists[0]
    return all(l == first for l in lists[1:])

# (Шаг 4)
def slice_with_step(lst: List[Any], start: Optional[int] = None,
                    stop: Optional[int] = None, step: Optional[int] = None) -> List[Any]:
    if step == 0:
        raise ValueError("step must not be zero")
    if step is None:
        step = 1
    return lst[start:stop:step]

# (Шаг 5)
def create_list(kind: str = 'range', count: int = 10, start: int = 0,
                step: int = 1, generator: Optional[callable] = None) -> List[Any]:
    if count < 0:
        raise ValueError('count must be non-negative')
    if kind == 'range':
        return [start + i * step for i in range(count)]
    elif kind == 'random':
        return [random.randint(0, max(1, count * 10)) for _ in range(count)]
    elif kind == 'generator':
        if generator is None:
            raise ValueError('generator must be provided for kind="generator"')
        return [generator(i) for i in range(count)]
    else:
        raise ValueError('unknown kind')

# (Шаг 6)
def insert_into_list(lst: List[Any], index: int, value: Any) -> List[Any]:
    if index >= len(lst):
        lst.append(value)
    else:
        lst.insert(index, value)
    return lst

# (Шаг 7)
def merge_and_sort(*lists: List[Any], key: Optional[callable] = None, reverse: bool = False) -> List[Any]:
    merged = []
    for l in lists:
        merged.extend(l)
    return sorted(merged, key=key, reverse=reverse)

# (Шаг 8)
def make_and_check_list(initial: Optional[List[int]] = None) -> Dict[str, Any]:
    lst = initial if initial is not None else [random.randint(0, 5) for _ in range(random.randint(1, 10))]
    result = {'original': lst.copy()}
    while len(lst) % 2 == 0:
        result.setdefault('steps', []).append(f'len={len(lst)} even, modifying')
        lst.append(random.randint(0, 5))
    mid_index = len(lst) // 2
    center_value = lst[mid_index]
    count_same = sum(1 for x in lst if x == center_value)
    result.update({'final_list': lst, 'center_index': mid_index,
                   'center_value': center_value, 'count_same_as_center': count_same})
    return result

# (Шаг 9)
def extend_with_limit(base: List[Any], *others: List[Any], limit: int = 50) -> List[Any]:
    for o in others:
        base.extend(o)
        if len(base) > limit:
            del base[limit:]
            break
    return base

# (Шаг 10)

def sort_by_natural(lst: List[Any]) -> List[Any]:
    return sorted(lst)

def sort_by_length(lst: List[Iterable]) -> List[Iterable]:
    return sorted(lst, key=lambda x: len(x))

def sort_by_sum_desc(lst: List[Iterable]) -> List[Iterable]:
    sums = list(map(sum, lst))
    paired = list(zip(sums, lst))
    paired.sort(key=lambda p: p[0], reverse=True)
    return [p[1] for p in paired]

def sort_by_first_element(lst: List[Iterable]) -> List[Iterable]:
    def first_or_none(x):
        try:
            return x[0]
        except Exception:
            return None
    keys = list(map(first_or_none, lst))
    paired = list(zip(keys, lst))
    paired.sort(key=lambda p: (p[0] is None, p[0]))
    return [p[1] for p in paired]

def sort_by_stringified(lst: List[Any]) -> List[Any]:
    strs = list(map(str, lst))
    paired = list(zip(strs, lst))
    paired.sort(key=lambda p: p[0])
    return [p[1] for p in paired]

def sort_by_custom_key(lst: List[Any], key_func: callable) -> List[Any]:
    return sorted(lst, key=key_func)

# (Шаг 11)
def pop_min(lst: List[Any]) -> Any:
    if not lst:
        return None
    min_val = min(lst)
    lst.remove(min_val)
    return min_val

# (Шаг 12)
def tuples_concat(*tuples: Tuple[Any, ...]) -> Tuple[Any, ...]:
    return tuple(itertools.chain.from_iterable(tuples))

def tuple_stats(tup: Tuple[Any, ...]) -> Dict[str, Any]:
    return {'length': len(tup), 'unique_count': len(set(tup)), 'unique_values': tuple(sorted(set(tup), key=lambda x: str(x)))}


# (Шаг 13)
def tuple_types(*values: Any) -> Tuple[type, ...]:
    return tuple(type(v) for v in values)


# (Шаг 14)
def tuple_contains(tup: Tuple[Any, ...], element: Any) -> bool:
    return element in tup


# (Шаг 15)
def make_2d_list(*lists: List[Any], fill: Any = None) -> List[List[Any]]:
    if len(lists) == 1:
        lst = lists[0]
        n = 3
        return [lst[i:i+n] for i in range(0, len(lst), n)]
    else:
        maxlen = max(len(l) for l in lists)
        matrix = []
        for l in lists:
            row = list(l) + [fill] * (maxlen - len(l))
            matrix.append(row)
        return matrix


# (Шаг 16)
def dict_keys_sorted(d: Dict[Any, Any]) -> List[Any]:
    return sorted(d.keys(), key=lambda x: str(x))

def dict_values_sum_if_numeric(d: Dict[Any, Any]) -> float:
    total = 0.0
    for v in d.values():
        if isinstance(v, (int, float)):
            total += v
    return total

def dict_invert(d: Dict[Any, Any]) -> Dict[Any, List[Any]]:
    res: Dict[Any, List[Any]] = {}
    for k, v in d.items():
        key = v if isinstance(v, (int, float, str, tuple)) else str(v)
        res.setdefault(key, []).append(k)
    return res

# (Шаг 17)
def count_key_occurrences(key: Any, *dicts: Dict[Any, Any]) -> int:
    return sum(1 for d in dicts if key in d)

# (Шаг 18)
def find_in_nested_dict(d: Dict[Any, Any], target_keys: Iterable[Any]) -> Dict[Any, Any]:
    found = []
    def dfs(obj, depth):
        if isinstance(obj, dict):
            if not obj:  
                return
            for k, v in obj.items():
                if isinstance(v, dict):
                    dfs(v, depth+1)
                else:
                    found.append((depth+1, k, v))
        elif isinstance(obj, list):
            for item in obj:
                dfs(item, depth+1)
    dfs(d, 0)
    if not found:
        return {}
    max_depth = max(depth for depth, _, _ in found)
    res = {}
    for depth, k, v in found:
        if depth == max_depth and k in target_keys:
            res[k] = v
    return res or None


# (Шаг 19)
def run_all():
    results = {}
    # 1
    lst = [1, 2, 3, 4]
    results['reverse_list'] = reverse_list(lst)
    # 2
    l2 = [0, 1, 2, 3]
    results['modify_list_values'] = modify_list_values(l2.copy(), {1: 99, -1: 7})
    # 3
    results['are_all_lists_equal'] = are_all_lists_equal([1,2], [1,2], [1,2])
    # 4
    results['slice_with_step'] = slice_with_step([0,1,2,3,4,5], 1, None, 2)
    # 5
    results['create_list'] = create_list('range', 5, 10, 2)
    # 6
    i_lst = [0,1,2]
    results['insert_into_list'] = insert_into_list(i_lst.copy(), 1, 'X')
    # 7
    results['merge_and_sort'] = merge_and_sort([3,1], [2], [0,5])
    # 8
    results['make_and_check_list'] = make_and_check_list([1,2,3])
    # 9
    results['extend_with_limit'] = extend_with_limit([1,2], [3,4,5], limit=4)
    # 10
    results['sort_by_natural'] = sort_by_natural([3,1,2])
    results['sort_by_length'] = sort_by_length([[1,2,3], [1], [1,2]])
    results['sort_by_sum_desc'] = sort_by_sum_desc([[1,2], [5], [0,0,1]])
    results['sort_by_first_element'] = sort_by_first_element([[9], [], [2,3]])
    results['sort_by_stringified'] = sort_by_stringified([10, '2', 'a'])
    results['sort_by_custom_key'] = sort_by_custom_key(['aa', 'b', 'c'], key_func=len)
    # 11
    p_lst = [5,1,3]
    results['pop_min'] = pop_min(p_lst)
    # 12
    results['tuples_concat'] = tuples_concat((1,2), ('a',))
    results['tuple_stats'] = tuple_stats((1,2,2,3))
    # 13
    results['tuple_types'] = tuple_types(1, 'a', 3.14, None)
    # 14
    results['tuple_contains'] = tuple_contains((1,2,3), 2)
    # 15
    results['make_2d_list_single'] = make_2d_list([1,2,3,4,5])
    results['make_2d_list_multi'] = make_2d_list([1,2], [3,4,5])
    # 16
    d = {'a':1, 'b':2, 'c':'x'}
    results['dict_keys_sorted'] = dict_keys_sorted(d)
    results['dict_values_sum_if_numeric'] = dict_values_sum_if_numeric(d)
    results['dict_invert'] = dict_invert(d)
    # 17
    results['count_key_occurrences'] = count_key_occurrences('name', {'name':'a'}, {'x':1}, {'name':'b'})
    # 18
    nested = {'lvl1': {'lvl2': {'target': 42}, 'lvl2b': {'other': 1}}, 'rootval': 0}
    results['find_in_nested_dict'] = find_in_nested_dict(nested, ['target', 'other'])
    return results