# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    three, five, seven = 3, 5, 7
    ans = n // three
    ans += n // five
    ans += n // seven
    ans -= n // (three * five)
    ans -= n // (five * seven)
    ans -= n // (seven * three)
    ans += n // (three * five * seven)

    print(ans)


if __name__ == "__main__":
    main()
