# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ans = 1

    for i in range(1, n + 1):
        ans *= i
    
    print(ans)


if __name__ == "__main__":
    main()
