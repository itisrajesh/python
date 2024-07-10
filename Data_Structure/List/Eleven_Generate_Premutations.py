def generate_permutations(lst):
    """
    Description: Generate all permutations of a list.
    Input: {list: list}
    Output: {permutation: list[list]}
    """
    if len(lst) == 1:
        return [lst]
    else:
        perms = []
        for i in range(len(lst)):
            elem = lst[i]
            rest = lst[:i] + lst[i+1:]
            for p in generate_permutations(rest):
                perms.append([elem] + p)
        return perms

my_list = [1, 2, 3]
perms = generate_permutations(my_list)
print(perms)
