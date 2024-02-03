N, M, Q = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

info_A = dict()
info_B = dict()

for _ in range(Q):
    typ, player, card = input().split()
    card = int(card)
    player_name = (A, B)[player == 'B']
    info = (info_A, info_B)[player == 'B']
    if typ == '1':
        if card in player_name:
            info[card] = info.get(card, 0) + 1
        else:
            player_name.append(card)
    else:
        if card in info and info[card] > 0:
            info[card] = info.get(card) - 1
        else:
            player_name.remove(card)

    print(len(set(A).symmetric_difference(set(B))) + sum(info_A.values()) + sum(info_B.values()), end=' ')
