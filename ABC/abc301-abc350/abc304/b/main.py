# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    # 文字列で受け取って、先頭から4文字目以降を0に
    n = list(input().rstrip())
    d = len(n)

    if d > 3:
        for i in range(3, d):
            n[i] = "0"

    print("".join(n))


if __name__ == "__main__":
    main()
