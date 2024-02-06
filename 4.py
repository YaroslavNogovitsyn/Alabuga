N = int(input())
L = {value: key for value, key in enumerate(input().split(), 1)}
P = map(int, input().split())

children_parents = {0: 0}
language_barrier = {}

curr_parent = 0
for elem in P:
    if elem in children_parents:
        curr_parent = children_parents[elem]
        continue

    children_parents[elem] = curr_parent
    count = 0
    curr_lang = L[elem]
    curr_elem = elem
    while True:
        if children_parents[elem] == 0 or L[children_parents[elem]] == curr_lang:
            language_barrier[curr_elem] = count
            curr_parent = curr_elem
            break
        elem = children_parents[elem]
        count += 1

print(*language_barrier.values())
