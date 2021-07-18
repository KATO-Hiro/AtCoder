# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    d = dict()

    for i in range(k):
        if c[i] not in d.keys():
            d[c[i]] = 1
        else:
            d[c[i]] += 1
    
    size = len(d.keys())
    ans = size

    for j in range(n - k):
        d[c[j]] -= 1

        if d[c[j]] == 0:
            size -= 1

        if c[j + k] not in d.keys():
            d[c[j + k]] = 1
            size += 1
        else:
            if d[c[j + k]] == 0:
                size += 1
            d[c[j + k]] += 1
        
        ans = max(ans, size)

    print(ans)


if __name__ == "__main__":
    main()
