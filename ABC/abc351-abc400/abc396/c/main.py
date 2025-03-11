# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    b = sorted(list(map(int, input().split())), reverse=True)
    w = sorted(list(map(int, input().split())), reverse=True)
    inf = 10**18
    diff = n - m

    # 配列の長さが異なる場合は、ダミー値で揃える
    if diff > 0:
        w += [-inf] * diff
    elif diff < 0:
        b += [-inf] * -diff

    ans = 0

    for wi, bi in zip(w, b):
        if wi >= 0 and bi >= 0:
            ans += wi + bi
        elif wi < 0 and bi >= 0:
            ans += bi
        elif wi >= 0 and bi < 0:
            if wi + bi < 0:
                continue

            ans += wi + bi

    print(ans)


if __name__ == "__main__":
    main()
