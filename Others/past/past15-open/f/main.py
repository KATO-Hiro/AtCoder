# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    c = [(ai, i) for i, ai in enumerate(a)]
    # print(sorted(c))
    b = [0] * n

    for j, (ai, i) in enumerate(sorted(c), 1):
        b[i] = j

    print(*b)


if __name__ == "__main__":
    main()
