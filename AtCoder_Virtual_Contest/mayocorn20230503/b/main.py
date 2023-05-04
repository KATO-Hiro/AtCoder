# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    ans = list()

    for _ in range(h):
        ci = input().rstrip()
        ans.append(ci)
        ans.append(ci)
    
    for ci in ans:
        print(''.join(ci))


if __name__ == "__main__":
    main()
