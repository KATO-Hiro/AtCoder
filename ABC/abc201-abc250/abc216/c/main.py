# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ans = ""

    while n > 0:
        if n % 2 == 0:
            n //= 2
            ans += "B"
        else:
            n -= 1
            ans += "A"
    
    print(ans[::-1])


if __name__ == "__main__":
    main()
