# -*- coding: utf-8 -*-


def main():
    n = int(input())
    w = list(map(int, input().split()))
    ans = float('inf')

    for i in range(1, n):
        ans = min(ans, abs(sum(w[:i]) - sum(w[i:])))

    print(ans)


if __name__ == '__main__':
    main()
