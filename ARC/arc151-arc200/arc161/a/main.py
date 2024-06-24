# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    n = int(input())
    a = sorted(list(map(int, input().split())))
    b = [0] * n

    for i in range(0, n, 2):
        b[i] = a[i // 2]

    d = deque(a[n // 2 + 1 :])

    for j in range(0, n - 2, 2):
        while len(d) > 0:
            di = d.popleft()

            if di > b[j + 2]:
                b[j + 1] = di
                break

        if len(d) == 0 and b[j + 1] == 0:
            print("No")
            exit()

    print("Yes")


if __name__ == "__main__":
    main()
