n = int(input())

children = [[] for _ in range(n + 1)]
roots = []

for employe in range(1, n + 1):
    boss = int(input())
    if boss == -1:
        roots.append(employe)
    else:
        children[boss].append(employe)


answer = 0

stack = [(root, 1) for root in roots]


while stack:

    v, depth = stack.pop()

    answer = max(answer, depth)

    for child in children[v]:
        stack.append((child, depth + 1))

print(answer)
