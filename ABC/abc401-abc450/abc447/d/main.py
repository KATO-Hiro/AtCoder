# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    s = input().rstrip()
    a = deque()
    b = deque()
    c = deque()

    for i, si in enumerate(s):
        if si == "A":
            a.append(i)
        elif si == "B":
            b.append(i)
        elif si == "C":
            c.append(i)

    ans = 0

    for bi in b:
        if not a or a[0] > bi:
            continue

        while c and c[0] < bi:
            c.popleft()

        if (a and a[0] < bi) and (c and c[0] > bi):
            ans += 1

            a.popleft()
            c.popleft()

    print(ans)


if __name__ == "__main__":
    main()
