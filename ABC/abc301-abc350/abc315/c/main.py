# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    fs = [tuple(map(int, input().split())) for _ in range(n)]
    fs = sorted(fs, key=lambda x: x[1], reverse=True)
    fi, si = fs[0]
    ans = si
    # print(fs)
    # print(fi, ans)

    for fj, sj in fs[1:]:
        if fj != fi:
            ans = max(ans, sj + si)
        else:
            ans = max(ans, sj // 2 + si)

    print(ans)


if __name__ == "__main__":
    main()
