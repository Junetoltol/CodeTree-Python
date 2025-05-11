s, q = input().split()
q = int(q)
s = list(s)

for _ in range(q):
    cmd = input().split()
    if cmd[0] == '1':
        a, b = int(cmd[1]) - 1, int(cmd[2]) - 1
        s[a], s[b] = s[b], s[a]
    elif cmd[0] == '2':
        x, y = cmd[1], cmd[2]
        s = [y if ch == x else ch for ch in s]
    print(''.join(s))
