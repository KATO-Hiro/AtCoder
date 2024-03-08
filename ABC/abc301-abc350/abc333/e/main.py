# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n = int(input())
    tx = [tuple(map(int, input().split())) for _ in range(n)]
    monsters = defaultdict(int)
    used = list()
    now, k_min = 0, 0

    for ti, xi in tx[::-1]:
        if ti == 1:
            if monsters[xi] >= 1:
                monsters[xi] -= 1
                now -= 1
                used.append(1)
            else:
                used.append(0)
        else:
            monsters[xi] += 1
            now += 1

        k_min = max(k_min, now)

    if now > 0:
        print(-1)
    else:
        print(k_min)
        print(*used[::-1])


if __name__ == "__main__":
    main()
