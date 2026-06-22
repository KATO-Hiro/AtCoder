# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, s, k = map(int, input().split())
    e = list(map(int, input().split()))
    ans = 0

    for ei in e:
        if s >= ei:
            s += ei
        elif s + k >= ei:
            diff = ei - s
            k -= diff
            ans += diff
            s += ei + diff
        else:
            print(-1)
            exit()

    print(ans)


if __name__ == "__main__":
    main()
