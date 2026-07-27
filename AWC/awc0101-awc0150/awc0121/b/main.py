# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    k -= 1
    a = list(map(int, input().split()))
    b = sorted(a, reverse=True)
    ans = 0

    for bi in b:
        if bi < b[k]:
            break

        ans += 1

    print(ans)


if __name__ == "__main__":
    main()
