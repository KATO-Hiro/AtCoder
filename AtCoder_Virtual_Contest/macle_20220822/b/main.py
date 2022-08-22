# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    w = list(map(int, input().split()))
    ws = sorted([(wi, si) for si, wi in zip(s, w)])
    count = s.count("1")
    ans = count

    for i in range(n):
        wi, si = ws[i]

        if si == "1":
            count -= 1
        else:
            count += 1
        
        if (i < n - 1) and (ws[i][0]) == (ws[i + 1][0]):
            continue

        ans = max(ans, count)

    print(ans)


if __name__ == "__main__":
    main()
