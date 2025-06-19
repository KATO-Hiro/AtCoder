# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    d = deque(a)
    ans = 0

    while len(d) > 1:
        aj = d.pop()
        ai = d[0]
        result = aj % ai
        ans += 1

        if result != 0:
            d.appendleft(result)

    print(ans)


if __name__ == "__main__":
    main()
