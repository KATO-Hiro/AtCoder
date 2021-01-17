# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans = 0
    a_max = 0

    for ai, bi in zip(a, b):
        a_max = max(a_max, ai)
        ans = max(ans, a_max * bi)
        print(ans)


if __name__ == "__main__":
    main()
