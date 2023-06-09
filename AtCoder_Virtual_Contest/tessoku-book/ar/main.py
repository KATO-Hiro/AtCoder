# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())
    a = [i for i in range(1, n + 1)]
    rev = False

    for _ in range(q):
        qi = list(map(int, input().split()))

        if qi[0] == 1:
            x, y = qi[1:]
            x -= 1

            if rev:
                a[n - x - 1] = y
            else:
                a[x] = y
        elif qi[0] == 2:
            if rev:
                rev = False
            else:
                rev = True
        else:
            x = qi[1] - 1

            if rev:
                print(a[n - x - 1])
            else:
                print(a[x])


if __name__ == "__main__":
    main()
