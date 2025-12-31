# -*- coding: utf-8 -*-


def solve():
    first, second, third = list(sorted(list(map(int, input().split()))))
    inf = 10**18
    ans = inf

    for _ in range(3):
        # 不変量に着目: 1回の操作での増分は mod 3 で変わらない
        if second % 3 == third % 3:
            ans = min(ans, max(second, third))

        # rotate
        first, second, third = second, third, first

    if ans == inf:
        ans = -1

    print(ans)


def main():
    import sys

    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
