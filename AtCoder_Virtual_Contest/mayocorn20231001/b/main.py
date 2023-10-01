# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n, m = map(int, input().split())
    d = defaultdict(list)

    for _ in range(m):
        pi, si = input().rstrip().split()
        d[pi].append(si)

    # print(d)
    ac_count, wa_count = 0, 0

    for values in d.values():
        if "AC" not in values:
            continue

        for value in values:
            if value == "WA":
                wa_count += 1
            else:
                ac_count += 1
                break

    print(ac_count, wa_count)


if __name__ == "__main__":
    main()
