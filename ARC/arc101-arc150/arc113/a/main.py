# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    k = int(input())
    ans = 0

    for a in range(1, k + 1):
        for b in range(1, k + 1):
            if a * b > k:
                break
            else:
                ans += k // (a * b)

    print(ans)


if __name__ == "__main__":
    main()
