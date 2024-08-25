# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    ans = 0

    while True:
        a.sort(reverse=True)
        a[0] -= 1
        a[1] -= 1

        ans += 1
        count = 0

        for ai in a:
            if ai > 0:
                count += 1

        if count <= 1:
            print(ans)
            exit()


if __name__ == "__main__":
    main()
