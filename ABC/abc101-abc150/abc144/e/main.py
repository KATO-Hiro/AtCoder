# -*- coding: utf-8 -*-


def calc_count(a, f, tmp_ans):
    count = 0

    for ai, fi in zip(a, f):
        new_ai = tmp_ans // fi
        count += max(0, ai - new_ai)

    return count


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    f = sorted(list(map(int, input().split())), reverse=True)

    ng = -1
    ok = 10 ** 12

    while (ok - ng) > 1:
        mid = (ok + ng) // 2

        if calc_count(a, f, mid) <= k:
            ok = mid
        else:
            ng = mid

    print(ok)


if __name__ == "__main__":
    main()
