# -*- coding: utf-8 -*-


def main():
    from itertools import product
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    m = [list(map(int, input().split()))[1:] for _ in range(m)]
    p = list(map(int, input().split()))
    patterns = list(product([True, False], repeat=n))
    ans = 0

    for pattern in patterns:
        flag = True

        for i, mi in enumerate(m):
            count = 0

            for mj in mi:
                if pattern[mj - 1]:
                    count += 1
            
            if count % 2 != p[i]:
                flag = False
                break
        
        if flag:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
