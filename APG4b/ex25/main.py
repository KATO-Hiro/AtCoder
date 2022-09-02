# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline


    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    s = input().rstrip().split()
    value_max = 49
    ans = set()

    if s[0] == "intersection":
        for i in range(0, value_max + 1):
            if i in a and i in b:
                ans.add(i)
    elif s[0] == "union_set":
        for ai in a:
            ans.add(ai)

        for bi in b:
            ans.add(bi)
    elif s[0] == "symmetric_diff":
        for i in range(0, value_max + 1):
            if i in a and i in b:
                continue

            if i in a:
                ans.add(i)
            if i in b:
                ans.add(i)
    elif s[0] == "subtract":
        x = int(s[1])
        a.remove(x)

        for ai in a:
            ans.add(ai)
    elif s[0] == "increment":
        for ai in a:
            if ai == 49:            
                ai = 0
            else:
                ai += 1

            ans.add(ai)
    elif s[0] == "decrement":
        for ai in a:
            if ai == 0:            
                ai = 49
            else:
                ai -= 1

            ans.add(ai)

    print(*sorted(ans))


if __name__ == "__main__":
    main()
