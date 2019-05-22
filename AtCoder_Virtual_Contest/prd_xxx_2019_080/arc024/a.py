# -*- coding: utf-8 -*-


def main():
    from collections import Counter

    l, r = map(int, input().split())
    ls = Counter(list(map(int, input().split())))
    rs = Counter(list(map(int, input().split())))
    ans = 0

    for lkey in ls.keys():
        for rkey in rs.keys():
            if lkey == rkey:
                ans += min(ls[lkey], rs[rkey])

    print(ans)


if __name__ == '__main__':
    main()
