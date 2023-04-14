# -*- coding: utf-8 -*-


def main():
    from string import ascii_uppercase
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    alpha = ascii_uppercase

    for i in range(h):
        ans = ""

        for j in range(w):
            ai = a[i][j]

            if ai == 0:
                ans += "."
            else:
                ans += alpha[ai - 1]
    
        print(ans)


if __name__ == "__main__":
    main()
