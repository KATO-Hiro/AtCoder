# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, t = map(int, input().split())
    ans = float("inf")

    for i in range(n):
        ci, ti = map(int, input().split())

        if ti <= t:
            ans = min(ans, ci)
    
    if ans == float("inf"):
        print("TLE")
    else:
        print(ans)


if __name__ == "__main__":
    main()
