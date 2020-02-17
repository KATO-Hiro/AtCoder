# -*- coding: utf-8 -*-


def main():
    from collections import Counter

    n = int(input())
    s = [input() for _ in range(n)]
    c = sorted(Counter(s).items(), key=lambda x: x[1], reverse=True)
    max_value = c[0][1]
    ans = list()

    for key, value in c:
        if value == max_value:
            ans.append(key)

    for a in sorted(ans):
        print(a)


if __name__ == '__main__':
    main()
