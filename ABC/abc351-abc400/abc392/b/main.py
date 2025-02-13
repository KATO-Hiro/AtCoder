# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = set(map(int, input().split()))
    ans = list()

    for i in range(1, n + 1):
        if i in a:
            continue

        ans.append(i)

    print(len(ans))
    print(*ans)


if __name__ == "__main__":
    main()
