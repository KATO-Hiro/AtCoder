# -*- coding: utf-8 -*-


def main():
    from collections import Counter

    n = int(input())
    s = sorted(Counter([input() for _ in range(n)]).items(), key=lambda x: x[1], reverse=True)
    print(s[0][0])


if __name__ == '__main__':
    main()
