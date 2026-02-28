# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(lambda x: int(x) - 1, input().split()))
    ans = [i for i in range(n)]

    for i in range(n - 1, -1, -1):
        if i != a[i]:
            ans[i] = ans[a[i]]

    ans = [ans_i + 1 for ans_i in ans]
    print(*ans)


if __name__ == "__main__":
    main()
