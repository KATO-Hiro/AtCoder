# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = list(map(int, input().split()))
    t = set()

    for a in range(1, 400):
        for b in range(1, 400):
            si = 4 * a * b + 3 * (a + b)
            
            if si <= 1000:
                t.add(si)
    
    ans = 0

    for si in s:
        if si not in t:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
