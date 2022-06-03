# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    p = list(map(int, input().split()))
    value_min = float("inf")
    ans = 0

    for i, pi in enumerate(p):
        value_min = min(value_min, pi)

        if pi == value_min:
            ans += 1
    
    print(ans)


if __name__ == "__main__":
    main()
