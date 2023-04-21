# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    ab = list()
    ans = 0
    
    for _ in range(n):
        ai, bi = map(int, input().split())
        ab.append((ai, bi))

    for ai, bi in sorted(ab):
        ci = min(m, bi)
        ans += ai * ci
        m -= min(m, ci)

        if m == 0:
            break
    
    print(ans)


if __name__ == "__main__":
    main()
