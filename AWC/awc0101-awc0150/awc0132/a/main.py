# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, p = map(int, input().split())
    h = list(map(int, input().split()))
    cur_p = p
    ans = 0

    for hi in h:
        if cur_p >= hi:
            cur_p -= hi
            ans += 1
        else:
            cur_p += hi

    print(ans)


if __name__ == "__main__":
    main()
