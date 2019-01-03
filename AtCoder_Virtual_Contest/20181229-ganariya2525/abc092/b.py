# -*- coding: utf-8 -*-


def main():
    n = int(input())
    d, x = map(int, input().split())
    a = [int(input()) for _ in range(n)]
    choco = [1 for _ in range(100 + 1)]
    ans = x

    for i in range(n):
        ans += sum(choco[:d:a[i]])

    print(ans)


if __name__ == '__main__':
    main()
