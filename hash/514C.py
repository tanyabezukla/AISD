n, m = map(int, input().split())

save = set()

for _ in range(n):
    save.add(input().strip())

for _ in range(m):
    s = list(input().strip())

    found = False

    for i in range(len(s)):
        old = s[i]

        for ch in "abc":
            if ch == old:
                continue

            s[i] = ch
            candidate = "".join(s)

            if candidate in save:
                found = True
                break

        s[i] = old

        if found:
            break

    print("YES" if found else "NO")
