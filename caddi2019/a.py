# -*- coding: utf-8 -*-


def main():
    l, n, m = map(int, input().split())
    rs = list()
    ps = list()
    abcd = list()

    for i in range(n):
        ri, pi = map(int, input().split())
        rs.append(ri)
        ps.append(pi)

    for j in range(m):
        a, b, c, d = map(int, input().split())
        abcd.append((a, b, c, d))

    print(sorted(abcd, key=lambda x: x[0] + x[1] + x[2], reverse=True))


if __name__ == '__main__':
    main()
