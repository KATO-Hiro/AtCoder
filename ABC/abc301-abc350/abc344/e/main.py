# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    next = defaultdict(int)
    prev = defaultdict(int)

    b = [0] + a + [-1]
    c = [0] + a[::-1] + [-1]

    for key, value in zip(b, b[1:]):
        next[key] = value

    for key, value in zip(c, c[1:]):
        prev[key] = value

    q = int(input())

    for _ in range(q):
        qi = list(map(int, input().split()))

        if qi[0] == 1:
            _, x, y = qi

            z = next[x]
            next[y] = z
            next[x] = y

            prev[y] = x
            prev[z] = y
        else:
            _, x = qi

            y, z = prev[x], next[x]

            if y == -1:
                next[0] = z
            else:
                next[y] = z

            if z == -1:
                prev[0] = y
            else:
                prev[z] = y

            del prev[x]
            del next[x]

    ans = list()
    pos = 0

    while next[pos] != -1:
        ans.append(next[pos])
        pos = next[pos]

    print(*ans)


if __name__ == "__main__":
    main()
