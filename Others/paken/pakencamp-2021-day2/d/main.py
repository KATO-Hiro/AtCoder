# -*- coding: utf-8 -*-


def main():
    from collections import Counter
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    c = Counter(a)
    ans_min = c.most_common()[-1][1]
    ans_max = c.most_common()[0][1]

    if len(c.keys()) != m:
        ans_min = 0
    
    print(ans_min, ans_max)


if __name__ == "__main__":
    main()
