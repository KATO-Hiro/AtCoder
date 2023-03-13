# -*- coding: utf-8 -*-


def main():
    from itertools import combinations
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    patterns = [i for i in range(h + w - 2)]
    ans = 0

    for pattern in combinations(list(patterns), r=w - 1):
        x, y = 0, 0
        numbers = [a[y][x]]

        for i in range(h + w - 2):
            if i in pattern:
                x += 1
            else:
                y += 1
            
            numbers.append(a[y][x])
        
        if len(numbers) == len(set(numbers)):
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
