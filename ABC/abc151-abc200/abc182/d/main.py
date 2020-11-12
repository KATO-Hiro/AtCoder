# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    summed = 0
    max_summed = 0
    pre_summed = 0
    ans = 0

    # See:
    # https://www.youtube.com/watch?v=l_-Eh5BP-wE&feature=youtu.be
    for ai in a:
        summed += ai
        max_summed = max(max_summed, summed)
        ans = max(ans, pre_summed + max_summed)

        pre_summed += summed

    print(ans)


if __name__ == "__main__":
    main()
