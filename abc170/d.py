# -*- coding: utf-8 -*-


def main():
    from collections import deque
    import sys
    input = sys.stdin.readline

    # n = int(input())
    # a = sorted(set(list(map(int, input().split()))))
    # m = len(a)
    # used = [False for _ in range(m)]
    # d = deque(a)
    # i = 0
    # ans = 0

    # while i < m:
    #     if used[i]:
    #         continue

    #     size = len(d)

    #     for j in range(size):
    #         di = d.popleft()

    #         if di % a[i] == 0:
    #             used[a.index(di)] = True
    #         else:
    #             d.append(di)

    #     ans += 1
    #     i += 1

    # print(ans + len(d))


if __name__ == '__main__':
    main()
