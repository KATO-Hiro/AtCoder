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
    
    if len(odd) == 1 and len(even) == 1:
        print(-1)
    elif len(odd) == 0:
        even = sorted(even, reverse=True)
        print(sum(even[:2]))
    elif len(even) == 0:
        odd = sorted(odd, reverse=True)
        print(sum(odd[:2]))
    else:
        even = sorted(even, reverse=True)
        odd = sorted(odd, reverse=True)
        print(max(sum(even[:2]), sum(odd[:2])))


if __name__ == "__main__":
    main()
