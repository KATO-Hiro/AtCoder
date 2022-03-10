# -*- coding: utf-8 -*-


def main():
    from collections import Counter
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)
    ans = 0
    max_number = 10 ** 5

    for i in range(1, max_number // 2):
        if i in c.keys() and (max_number - i) in c.keys():
            ans += c[i] * c[max_number - i]
    
    if max_number // 2 in c.keys():
        ans += c[max_number // 2] * (c[max_number // 2] - 1) // 2
    
    print(ans)


if __name__ == "__main__":
    main()
