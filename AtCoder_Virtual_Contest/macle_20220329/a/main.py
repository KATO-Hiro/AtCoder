# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    h = sorted(list(map(int, input().split())), reverse=True)
    ans = 0

    for hi in h:
        if k > 0:
            k -= 1
        else:
            ans += hi
    
    print(ans)


if __name__ == "__main__":
    main()
