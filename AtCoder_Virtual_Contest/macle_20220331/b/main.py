# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = list(input().rstrip())
    r = s.count("R")
    g = s.count("G")
    b = s.count("B") 
    ans = r * g * b

    for i in range(n):
        for j in range(i + 1, n):
            k = 2 * j - i

            if k >= n:
                continue

            if len(set([s[i], s[j], s[k]])) == 3:
                ans -= 1
    
    print(ans)



if __name__ == "__main__":
    main()
