# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    ans = 0
    n = int(input())

    for i in range(n):
        ans += n / (n - i)
    
    print(ans)


if __name__ == "__main__":
    main()
