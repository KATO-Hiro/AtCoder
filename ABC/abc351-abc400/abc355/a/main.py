# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    ab = set(map(int, input().split()))
    ans = list(ab ^ set([1, 2, 3]))

    if len(ans) == 1:
        print(ans[0])
    else:
        print(-1)


if __name__ == "__main__":
    main()
