# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, l, t, x = map(int, input().split())
    a = [0 for _ in range(n)]
    b = [0 for _ in range(n)]
    ans = 0
    load_time = 0

    for i in range(n):
        ai, bi = map(int, input().split())
        a[i] = ai
        b[i] = bi

    for ai, bi in zip(a, b):
        if bi >= l and ai > t:
            print("forever")
            exit()

    for ai, bi in zip(a, b):
        if bi < l:
            ans += ai
            load_time = 0
        else:
            if load_time + ai < t:
                ans += ai
                load_time += ai
            elif load_time + ai == t:
                ans += ai
                ans += x
                load_time = 0
            else:
                ans += t - load_time
                ans += x
                ans += ai
                load_time = ai

                if load_time == t:
                    ans += x
                    load_time = 0

    print(ans)


if __name__ == "__main__":
    main()
