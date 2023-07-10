# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    k = int(input())
    mod = k
    seven = 7
    ans = -1

    for i in range(1, 2 * k + 1):
        if seven % mod == 0:
            ans = i
            break

        seven *= 10
        seven += 7
        seven %= mod

    print(ans)


if __name__ == "__main__":
    main()
