# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ans = 0

    for _ in range(n):
        si = input().rstrip()

        if si == "Takahashi":
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
