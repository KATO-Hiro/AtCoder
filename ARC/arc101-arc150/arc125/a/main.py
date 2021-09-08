# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))

    inf = float("inf")
    pos_min = inf

    for i in range(n):
        if s[0] != s[i]:
            pos_min = min(pos_min, i, n - i)

    first_switched = False
    flag = s[0]
    ans = m

    for ti in t:
        if first_switched:
            if ti != flag:
                ans += 1
                flag = ti

        else:
            if ti != flag:
                ans += pos_min

                flag = ti
                first_switched = True
    
    if ans == inf:
        print(-1)
    else:
        print(ans)


if __name__ == "__main__":
    main()
