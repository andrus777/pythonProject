def calculate_structure_sum(args):
    res = 0
    for arg in args:
        if isinstance(arg, (int, float)):
            res = res + arg
        if isinstance(arg, str):
            res = res + len(arg)
        if isinstance(arg, list):
            res = res + calculate_structure_sum(arg)
        if isinstance(arg, tuple):
            res = res + calculate_structure_sum(arg)
        if isinstance(arg, set):
            res = res + calculate_structure_sum(arg)
        if isinstance(arg, dict):
            res = res + calculate_structure_sum(arg.keys())
            res = res + calculate_structure_sum(arg.values())
    return res


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)