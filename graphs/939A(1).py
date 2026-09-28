
n = int(input())

f = [0] + list(map(int, input().split()))

found = False

for i in range(1, n + 1):
    first = f[i]
    second = f[first]
    third = f[second]

    if third == i:
        found = True
        break

if found:
    print("YES")
else:
    print("NO")