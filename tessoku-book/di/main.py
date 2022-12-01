# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    s = input().rstrip()
    count = s.count("1")

    # 0, 0 / 1, 1で豆電球が2個ずつon / offに
    # 0, 1 / 1, 0のときは変わらない 
    # 偶奇性を活用できそう
    if abs(count - k) % 2 == 0:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
