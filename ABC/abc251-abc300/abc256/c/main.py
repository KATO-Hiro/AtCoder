# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    hw = list(map(int, input().split()))
    hi = hw[:3]
    wi = hw[3:]
    upper = 31
    ans = 0

    for a in range(1, upper):
        for b in range(1, upper):
            for d in range(1, upper):
                for e in range(1, upper):
                    c = hi[0] - (a + b)
                    f = hi[1] - (d + e)

                    g = wi[0] - (a + d)
                    h = wi[1] - (b + e)
                    
                    i1 = hi[2] - (g + h)
                    i2 = wi[2] - (c + f)
    
                    if min([c, f, g, h, i1, i2]) >= 1 and (i1 == i2):
                        ans += 1

    print(ans)


if __name__ == "__main__":
    main()
