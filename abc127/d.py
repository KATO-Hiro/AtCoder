# -*- coding: utf-8 -*-


def main():
    from collections import Counter

    n, m = map(int, input().split())
    a = Counter(list(map(int, input().split())))

    for i in range(m):
        bi, ci = map(int, input().split())
        a[ci] += bi

    cards = sorted(a.items(), key=lambda x: x[0], reverse=True)
    ans = 0

    for number, count in cards:
        if n > count:
            ans += number * count
            n -= count
        else:
            ans += number * n
            print(ans)
            exit()



if __name__ == '__main__':
    main()
