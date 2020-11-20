# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    ans, count_max = 0, 0

    for i in range(2, 1000 + 1):
        count = 0

        for ai in a:
            if ai % i == 0:
                count += 1

        if count > count_max:
            ans, count_max = i, count

    print(ans)


if __name__ == "__main__":
    main()
