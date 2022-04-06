# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    n = len(s)
    t = s + s
    ans = set()

    for i in range(n):
        ans.add(t[i:i+n])
    
    ans = sorted(ans)

    print(ans[0])
    print(ans[-1])


if __name__ == "__main__":
    main()
