# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    r = [0 for _ in range(n)]
    g = [0 for _ in range(n)]
    b = [0 for _ in range(n)]

    for i, si in enumerate(s):
        if si == "R":
            r[i] = 1
        elif si == "G":
            g[i] = 1
        else:
            b[i] = 1
    
    r = list(accumulate(r))
    g = list(accumulate(g))
    b = list(accumulate(b))
    ans = 0

    for i in range(n - 2):
        si = s[i]

        for j in range(i + 1, n - 1):
            sj = s[j]
            k = 2 * j - i

            if (si == "R" and sj == "G") or (si == "G" and sj == "R"):
                ans += b[n - 1] - b[j]

                if k < n and s[k] == "B":
                    ans -= 1
            elif (si == "R" and sj == "B") or (si == "B" and sj == "R"):
                ans += g[n - 1] - g[j]

                if k < n and s[k] == "G":
                    ans -= 1
            elif (si == "G" and sj == "B") or (si == "B" and sj == "G"):
                ans += r[n - 1] - r[j]

                if k < n and s[k] == "R":
                    ans -= 1

    print(ans)


if __name__ == "__main__":
    main()
