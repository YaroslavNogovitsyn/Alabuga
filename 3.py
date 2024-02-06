info = []

N, M, Q = map(int, input().split())
keys = input().split()

for _ in range(N):
    values = map(int, input().split())
    info.append(dict(zip(keys, values)))

for ind in range(Q):
    name, sign, value = input().split()
    info = tuple(filter(lambda x: eval(f'{x[name]} {sign} {value}'), info))

print(sum(map(lambda x: sum(x.values()), info)))
