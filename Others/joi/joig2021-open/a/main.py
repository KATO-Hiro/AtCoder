# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    abc = list(map(int, input().split()))
    max_value = max(abc)
    ans = 0

    for alpha in abc:
        ans += max_value - alpha

    print(ans)


if __name__ == "__main__":
    main()
