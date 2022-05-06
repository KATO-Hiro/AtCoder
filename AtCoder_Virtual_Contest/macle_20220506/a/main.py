# -*- coding: utf-8 -*-


def main():
    from itertools import product
    import sys

    input = sys.stdin.readline

    n = input().rstrip()
    size = len(n)
    patterns = product([0, 1], repeat=size)
    ans = 0

    for pattern in patterns:
        case1 = list()
        case2 = list()

        for i, p in enumerate(pattern):
            if p == 0:
                case1.append(n[i])
            else:
                case2.append(n[i])
        
        if len(case1) == 0 or len(case2) == 0:
            continue
        if case1[0] == '0' or case2[0] == '0':
            continue
        
        ans = max(ans, int(''.join(sorted(case1, reverse=True))) * int(''.join(sorted(case2, reverse=True))))

    print(ans)


if __name__ == "__main__":
    main()
