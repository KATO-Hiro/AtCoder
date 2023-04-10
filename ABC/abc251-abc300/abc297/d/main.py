# -*- coding: utf-8 -*-

ans = 0


def main():
    import sys
    sys.setrecursionlimit(10 ** 8)

    input = sys.stdin.readline

    a, b = map(int, input().split())


    def rec(x, y):
        global ans

        if x < y:
            x, y = y, x

        if x == y:
            return ans
        elif y == 0:
            ans -= 1
            return ans
        else:
            ans += x // y
            rec(y, x % y)
    
    rec(a, b)
    print(ans)
    

if __name__ == "__main__":
    main()
