t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    answer = n - 1

    for i in range(n - 2):
        if s[i] == s[i + 2]:
            answer -= 1

    print(answer)
