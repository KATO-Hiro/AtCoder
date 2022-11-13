# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    b = list(accumulate([0] + a))
    q = int(input())

    for _ in range(q):
        li, ri = map(int, input().split())
        total = ri - li + 1
        hit_count = b[ri] - b[li - 1]
        non_hit_count = total - hit_count

        if hit_count > non_hit_count:
            print("win")
        elif hit_count < non_hit_count:
            print("lose")
        else:
            print("draw")


if __name__ == "__main__":
    main()
