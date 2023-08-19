# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    st = [input().rstrip().split() for _ in range(n)]

    for i in range(n):
        si, ti = st[i]

        for j in range(i + 1, n):
            sj, tj = st[j]

            if si == sj and ti == tj:
                print("Yes")
                exit()

    print("No")


if __name__ == "__main__":
    main()
