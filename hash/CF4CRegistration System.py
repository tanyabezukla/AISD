
n = int(input())
users = {}

for _ in range(n):
    name = input()
    if name not in users:
        print("OK")
        users[name] = 0
    else:
        users[name] += 1
        print(f"{name}{users[name]}")

