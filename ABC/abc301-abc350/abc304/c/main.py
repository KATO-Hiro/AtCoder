# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    n, d = map(int, input().split())
    d = d**2
    xy = [tuple(map(int, input().split())) for _ in range(n)]
    ans = [False] * n
    q = deque([0])

    while q:
        cur = q.popleft()
        x_cur, y_cur = xy[cur]

        if ans[cur]:
            continue

        ans[cur] = True

        for i in range(n):
            if ans[i]:
                continue

            xi, yi = xy[i]

            if ((xi - x_cur) ** 2 + (yi - y_cur) ** 2) <= d:
                q.append(i)

    for ans_i in ans:
        if ans_i:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
