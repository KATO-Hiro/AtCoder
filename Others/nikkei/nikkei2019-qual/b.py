# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = input()
    b = input()
    c = input()
    ans = 0

    for i in range(n):
        s = set()
        s.add(a[i])
        s.add(b[i])
        s.add(c[i])

        if len(s) == 2:
            ans += 1
        elif len(s) == 3:
            ans += 2

    print(ans)


if __name__ == '__main__':
    main()
