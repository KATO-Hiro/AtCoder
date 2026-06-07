# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a2 = sorted([(i, ai) for i, ai in enumerate(a, 1)])
    b2 = sorted([(bj, j) for j, bj in enumerate(b, 1)])

    for ai, bi in zip(a2, b2):
        if ai != bi:
            print("No")
            exit()

    print("Yes")


if __name__ == "__main__":
    main()
