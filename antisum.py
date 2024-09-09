def antisum(m, start=1):
    if m == 0:
        return [[]]
    
    combinations = []
    for i in range(start, m + 1):
        for sub_combination in find_combinations(m - i, i + 1):
            combinations.append([i] + sub_combination)
    
    return combinations
