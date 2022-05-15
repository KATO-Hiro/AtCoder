# -*- coding: utf-8 -*-


def main():
    from itertools import product
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    n = int(s)
    digit = len(s)
    ans = set()

    for di in range(3, digit + 1):
        for p in product([3, 5, 7], repeat=di):
            if p.count(3) == 0:
                continue
            if p.count(5) == 0:
                continue
            if p.count(7) == 0:
                continue

            value = int(''.join(map(str, p)))

            if value <= n:
                ans.add(value)
    
    print(len(ans))


if __name__ == "__main__":
    main()
