# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, w = map(int, input().split())
    ab = list()

    for i in range(n):
        a, b = map(int, input().split())
        ab.append((a, b))
    
    ab = sorted(ab, key=lambda x: x[0], reverse=True)
    ans = 0

    for ai, bi in ab:
        if w - bi >= 0:
            w -= bi
            ans += ai * bi
        else:
            ans += ai * w
            break

    print(ans)


if __name__ == "__main__":
    main()
