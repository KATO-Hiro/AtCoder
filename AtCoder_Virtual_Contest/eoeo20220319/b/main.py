# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    l = int(input())
    ans = 1

    for i in range(l - 11, l):
        ans *= i
    
    for i in range(1, 12):
        ans //= i
    
    print(ans)


if __name__ == "__main__":
    main()
