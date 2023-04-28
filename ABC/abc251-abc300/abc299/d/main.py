# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    left, right = 1, n

    while right - left > 1:
        mid = (left + right) // 2
        print("?", mid, flush=True)

        s_mid = int(input())

        if s_mid == 0:
            left = mid
        else:
            right = mid
    
    p = left

    print("!", p, flush=True)


if __name__ == "__main__":
    main()
