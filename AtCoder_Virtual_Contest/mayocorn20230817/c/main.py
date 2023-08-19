# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ab = list()

    for _ in range(n):
        ai, bi = map(int, input().split())
        ab.append((bi, ai))

    ab = sorted(ab)
    # print(ab)

    prev_end = 0

    # for cur_cost, cur_end in ab:
    for cur_end, cur_cost in ab:
        if prev_end + cur_cost > cur_end:
            print("No")
            exit()
        else:
            prev_end += cur_cost

    print("Yes")


if __name__ == "__main__":
    main()
