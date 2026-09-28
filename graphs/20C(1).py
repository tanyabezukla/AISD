import heapq

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())

    graph[u].append((v, w))
    graph[v].append((u, w))


INF = float("inf")

dist = [INF] * (n + 1)
parent = [-1] * (n + 1)

dist[1] = 0

heap = [(0, 1)]


while heap:
    current_dist, v = heapq.heappop(heap)

    if current_dist != dist[v]:
        continue

    for to, weight in graph[v]:
        new_dist = current_dist + weight

        if new_dist < dist[to]:
            dist[to] = new_dist
            parent[to] = v

            heapq.heappush(heap, (new_dist, to))


if dist[n] == INF:
    print(-1)

else:
    path = []

    current = n

    while current != -1:
        path.append(current)
        current = parent[current]

    path.reverse()

    print(*path)