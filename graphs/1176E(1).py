t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    dist = [-1] * (n + 1)
    dist[1] = 0

    q = [1]
    index = 0

    while index < len(q):
        v = q[index]
        index += 1

        for to in graph[v]:
            if dist[to] == -1:
                dist[to] = dist[v] + 1
                q.append(to)

    even = []
    odd = []

    for v in range(1, n + 1):
        if dist[v] % 2 == 0:
            even.append(v)
        else:
            odd.append(v)

    if len(even) <= len(odd):
        answer = even
    else:
        answer = odd

    print(len(answer))
    print(*answer)