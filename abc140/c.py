# -*- coding: utf-8 -*-


def main():
    n = int(input())
    b = list(map(int, input().split()))
    ans = b[0] + b[-1]

    if n >= 3:
        for i in range(n - 2):
            ans += min(b[i], b[i + 1])

    print(ans)


if __name__ == '__main__':
    main()
