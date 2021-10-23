# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    xy = [tuple(map(int, input().split())) for _ in range(n)]
    ans = 0
    
    for i in range(n):
        x1, y1 = xy[i]

        for j in range(i + 1, n):
            x2, y2 = xy[j]

            for k in range(j + 1, n):
                x3, y3 = xy[k]

                if ((x1 - x3) * (y2 - y3)) != ((x2 - x3) * (y1 - y3)):
                    ans += 1
    
    print(ans)


if __name__ == "__main__":
    main()
