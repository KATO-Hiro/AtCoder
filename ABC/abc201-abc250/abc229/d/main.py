# -*- coding: utf-8 -*-


def main():
    s = input()
    n = len(s)
    k = int(input())
    r = 0
    count = 0
    a = [0 for _ in range(n)]
    ans = 0

    for index, si in enumerate(s):
        if si == '.':
            a[index] = 1
        
    for l in range(n):
        while r < n and count + a[r] <= k:
            count += a[r]
            r += 1
        
        ans = max(ans, r - l)

        count -= a[l]

    print(ans)


if __name__ == "__main__":
    main()
