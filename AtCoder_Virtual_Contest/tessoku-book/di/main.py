# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    s = input().rstrip()
    on = s.count("1")

    # 操作によって、onの数は-2/0/+2の範囲でしか変わらない
    if on % 2 == k % 2:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
