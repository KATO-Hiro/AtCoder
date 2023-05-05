# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, a, b = map(int, input().split())
    ans = 0

    for i in range(1, n + 1):
        summed = 0

        for si in list(str(i)):
            summed += int(si)
        
        if a <= summed <= b:
            ans += i
    
    print(ans)


if __name__ == "__main__":
    main()
