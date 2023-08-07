# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b = input().rstrip().replace(".", "").split()
    ans = int(a) * int(b) // 100
    # print(a, b)
    print(ans)


if __name__ == "__main__":
    main()
