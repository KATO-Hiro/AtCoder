# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x = int(input())
    ans = 0

    for i in range(1, 10):
        for j in range(1, 10):
            k = i * j

            if k == x:
                continue

            ans += k

    print(ans)


if __name__ == "__main__":
    main()
