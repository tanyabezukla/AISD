
n, m = map(int, input().split())

cats = [0] + list(map(int, input().split()))

graph = [[] for i in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)


answer = 0


# текущая вершина, родитель, количество кошек подряд
stack = [(1, 0, 0)]


while stack:
    v, parent, consecutive = stack.pop()

    # обновляем количество кошек подряд
    if cats[v] == 1:
        consecutive += 1
    else:
        consecutive = 0

    # кошек подряд стало слишком много,
    # дальше по этой ветке идти бессмысленно
    if consecutive > m:
        continue

    # это лист мы дошли до ресторана
    if v != 1 and len(graph[v]) == 1:
        answer += 1
        continue

    # добавляем детей 
    for to in graph[v]:

        
        if to == parent:
            continue

        stack.append((to, v, consecutive))


print(answer)