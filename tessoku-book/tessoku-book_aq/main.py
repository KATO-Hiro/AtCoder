# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, l = map(int, input().split())
    ans = 0

    for _ in range(n):
        ai, bi = input().rstrip().split()
        ai = int(ai)

        if bi == "E":
            ans = max(ans, l - ai)
        else:
            ans = max(ans, ai)

    print(ans)
   

if __name__ == "__main__":
    main()
