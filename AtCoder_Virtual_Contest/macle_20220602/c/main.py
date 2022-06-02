# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())

    if n % 2 == 1:
        print(0)
        exit()

    ans = 0
    p5 = 10

    while p5 <= n:
        ans += n // p5
        p5 *= 5
    
    print(ans)


if __name__ == "__main__":
    main()
