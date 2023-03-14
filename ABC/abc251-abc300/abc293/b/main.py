# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict
    import sys

    input = sys.stdin.readline
    
    n = int(input())
    a = [0] + list(map(int, input().split()))
    d = defaultdict(int)

    for i in range(1, n + 1):
        if d[i] == 0:
            d[a[i]] += 1
    
    ans = list()
    
    for i in range(1, n + 1):
        if d[i] == 0:
            ans.append(i)
    
    print(len(ans))
    print(*sorted(ans))
    

if __name__ == "__main__":
    main()
