# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    h = list(map(int, input().split()))[::-1]
    prev = h[0]
    ans = "Yes"

    for hi in h[1:]:
        if hi - prev > 1:
            ans = "No"
            break
        else:
            prev = min(hi, prev)

    print(ans)


if __name__ == "__main__":
    main()
