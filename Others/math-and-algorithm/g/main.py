# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, x, y = map(int, input().split())
    ans = set()

    for i in range(1, n + 1):
        if i % x == 0 or i % y == 0:
            ans.add(i)
    
    print(len(ans))


if __name__ == "__main__":
    main()
