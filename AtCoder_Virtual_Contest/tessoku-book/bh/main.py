# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    n = int(input())
    a = [0] + list(map(int, input().split()))
    q = deque()
    ans = list()

    # d日目より前で、かつ、a[d] < a[j]となる場合をstackで管理
    for d in range(1, n + 1):
        if d >= 2:
            q.append((d - 1, a[d - 1]))

            while q and a[d] > q[-1][1]:
                q.pop()

        if len(q) == 0:
            ans.append(-1)
        else:
            ans.append(q[-1][0])

    print(*ans)


if __name__ == "__main__":
    main()
