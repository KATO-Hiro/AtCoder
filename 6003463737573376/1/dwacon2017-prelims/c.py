# -*- coding: utf-8 -*-


def main():
    from bisect import bisect_left

    n = int(input())
    a = [int(input()) for _ in range(n)]
    ride = [0 for _ in range(n)]
    group_members = [[0] for __ in range(4)]
    ans = [4 for _ in range(n)]

    for i in range(n):
        group_members[a[i] - 1].append(i)

    print(group_members)
    print(bisect_left(group_members[0], 1))
    # ride[0] = 1
    # ans[0] -= a[0]
    k = 0


if __name__ == '__main__':
    main()
