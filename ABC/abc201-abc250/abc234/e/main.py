# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x = int(input())
    ans = 2 * 10 ** 18

    for f in range(1, 9 + 1):
        for d in range(-9, 8 + 1):
            cur = 0
            i = f

            while (cur < x) and (0 <= i <= 9):
                cur = cur * 10 + i

                if cur >= x:
                    ans = min(ans, cur)
                    break

                i += d
    
    print(ans)


if __name__ == "__main__":
    main()
