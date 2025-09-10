# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    b = [k]

    # 操作を逆順に
    for _ in range(n):
        nb = list()

        for bi in b:
            value = bi // 2
            nb.append(value)
            nb.append(bi - value)

        b = nb

    m = 2**n

    if k % m == 0:
        print(0)
    else:
        print(1)

    print(*b)


if __name__ == "__main__":
    main()
