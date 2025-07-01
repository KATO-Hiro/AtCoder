# -*- coding: utf-8 -*-


def solve():
    n = int(input())
    s = list(map(int, input().split()))
    r = sorted(s[1:], reverse=True)
    prev = s[0]
    dominos = [s[0]]
    ok = True

    while len(r) >= 1:
        if s[-1] <= prev * 2:
            dominos.append(s[-1])
            break

        while len(r) >= 1 and r[-1] < prev:
            r.pop()

        tmp = -1

        while len(r) >= 1 and r[-1] <= 2 * prev:
            tmp = r.pop()

        if tmp == -1:
            ok = False
            break

        prev = tmp
        dominos.append(tmp)

    if ok:
        print(len(dominos))
    else:
        print(-1)


def main():
    import sys

    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
