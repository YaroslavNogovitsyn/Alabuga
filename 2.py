def list_to_dict(data: list) -> dict:
    return {key: data.count(key) for key in set(data)}


def merge_dicts(dict1: dict, dict2: dict) -> dict:
    result = dict(dict1)
    for key, value in dict2.items():
        if key in result:
            result[key] -= value
        else:
            result[key] = -value
    return result


N, M, Q = map(int, input().split())
A = list_to_dict(input().split())
B = list_to_dict(input().split())

all_values = merge_dicts(A, B)

for _ in range(Q):
    typ, player, card = input().split()

    if player == 'A':
        if typ == '1':
            all_values[card] = all_values.get(card, 0) + 1
        else:
            all_values[card] = all_values.get(card, 0) - 1
    else:
        if typ == '1':
            all_values[card] = all_values.get(card, 0) - 1
        else:
            all_values[card] = all_values.get(card, 0) + 1

    print(sum(map(lambda x: abs(all_values[x]), all_values)), end=' ')
