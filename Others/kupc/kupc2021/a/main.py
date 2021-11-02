# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = sorted(list(map(int, input().split())))
    t = int(input())
    ans = set()

    for si in s:
        p, q = divmod(si, t)
        ans.add(p)
    
    print(len(ans))


if __name__ == "__main__":
    main()
