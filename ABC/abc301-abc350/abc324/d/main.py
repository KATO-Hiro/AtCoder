# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = "".join(sorted(input().rstrip()))
    upper = 4 * 10**6
    ans = set()

    # 平方数は0も含む
    for i in range(upper):
        i = str(i**2).zfill(n)
        j = "".join(sorted(i))

        if j == s:
            ans.add(i)

    print(len(ans))


if __name__ == "__main__":
    main()
