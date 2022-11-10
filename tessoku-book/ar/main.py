# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())
    a = [i for i in range(1, n + 1)]
    count = 0

    for _ in range(q):
        qi = list(map(int, input().split()))

        if qi[0] == 1:
            x, y = qi[1], qi[2]

            if count % 2 == 0:
                a[x - 1] = y
            else:
                a[n - x] = y
        elif qi[0] == 2:
            count += 1
        else:
            x = qi[1]
        
            if count % 2 == 0:
                print(a[x - 1])
            else:
                print(a[n - x])


if __name__ == "__main__":
    main()
