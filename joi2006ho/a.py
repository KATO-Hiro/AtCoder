# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline
    p = list()

    n, m = map(int, input().split())
    t = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for index, si in enumerate(list(map(int, input().split()))):
            t[i][index] = si

    for i in range(m):
        count = 0

        for j in range(n):
            if t[j][i] == 1:
                count += 1

        p.append((i + 1, count))

    c = sorted(p, key=lambda x: (x[1], -x[0]), reverse=True)
    ans = list()

    for index, ci in c:
        ans.append(index)

    print(' '.join(map(str, ans)))


if __name__ == '__main__':
    main()
