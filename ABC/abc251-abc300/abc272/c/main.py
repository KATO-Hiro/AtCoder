# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    odd = list()
    even = list()

    for ai in a:
        if ai % 2 == 0:
            even.append(ai)
        else:
            odd.append(ai)
    
    ans = -1

    if len(odd) >= 2:
        odd = sorted(odd, reverse=True)
        ans = max(ans, (sum(odd[:2])))
    if len(even) >= 2:
        even = sorted(even, reverse=True)
        ans = max(ans, sum(even[:2]))

    print(ans)


if __name__ == "__main__":
    main()
