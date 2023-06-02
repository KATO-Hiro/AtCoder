# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import accumulate

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    b = [0] + list(accumulate(a))
    q = int(input())

    for _ in range(q):
        li, ri = map(int, input().split())
        win_count = b[ri] - b[li - 1]
        total = ri - li + 1

        if win_count * 2 > total:
            print("win")
        elif win_count * 2 < total:
            print("lose")
        else:
            print("draw")


if __name__ == "__main__":
    main()
