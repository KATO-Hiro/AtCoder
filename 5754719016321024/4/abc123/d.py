# -*- coding: utf-8 -*-


def main():
    x, y, z, k = map(int, input().split())
    a = sorted(list(map(int, input().split())), reverse=True)
    b = sorted(list(map(int, input().split())), reverse=True)
    c = sorted(list(map(int, input().split())), reverse=True)
    ac = list()

    for ai in a:
        for ci in c:
            ac.append(ai + ci)

    count = min(x * z, k)
    acs = sorted(ac, reverse=True)[:count]
    ans = list()

    for bi in b:
        for ac_i in acs:
            ans.append(bi + ac_i)

    for j in sorted(ans, reverse=True)[:k]:
        print(j)


if __name__ == '__main__':
    main()
