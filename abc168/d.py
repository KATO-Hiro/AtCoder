# -*- coding: utf-8 -*-


def main():
    from collections import deque
    import sys
    input = sys.stdin.readline

    n, m = map(int, input().split())
    p = [[] for _ in range(n)]
    d = deque()
    d.append(0)
    is_used = [False for _ in range(n)]
    is_used[0] = True
    ans = [0 for _ in range(n)]

    for i in range(m):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        p[ai].append(bi)
        p[bi].append(ai)

    while d:
        di = d.popleft()

        for e in p[di]:
            if is_used[e]:
                continue

            is_used[e] = True
            ans[e] = di + 1

            d.append(e)

    print('Yes')
    print('\n'.join(map(str, ans[1:])))


if __name__ == '__main__':
    main()
