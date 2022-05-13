# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b = map(int, input().split())
    ans = 0

    for _ in range(2):
        if a >= b:
            ans += a
            a -= 1
        else:
            ans += b
            b -= 1
    
    print(ans)


if __name__ == "__main__":
    main()
