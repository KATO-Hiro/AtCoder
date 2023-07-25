# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    r, n, m, l = map(int, input().split())
    s = list(map(int, input().split()))
    cur_round, cur_op, remain = 0, 0, n

    for si in s:
        if si > n:
            print("No")
            exit()

        cur_op += 1
        remain -= si

        if cur_op == m or remain == 0:
            cur_round += 1
            cur_op, remain = 0, n

        print(cur_round, cur_op, remain)

    if cur_round == r and cur_op == 0:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
