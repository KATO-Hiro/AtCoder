# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    upper = 10 ** 9
    ans = ["x"] * m 

    for i in range(m):
        if pow(n, i + 1) <= upper:
            ans[i] = "o"
        else:
            break

    print(''.join(ans))


if __name__ == "__main__":
    main()
