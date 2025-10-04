# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(list(map(int, input().split())))

    # 各項がxになる = 一つを固定して解の候補を列挙
    xs = sorted([a[0] ^ bi for bi in b])
    ans = set()

    for x in xs:
        c = sorted([ai ^ x for ai in a])

        if c == b:
            ans.add(x)

    size = len(ans)
    print(size)

    if size >= 1:
        print(*sorted(ans), sep="\n")


if __name__ == "__main__":
    main()
