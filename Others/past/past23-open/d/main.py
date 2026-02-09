# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = [input().rstrip() for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i == j or j == k or k == i:
                    continue

                ok = True

                if s[i] + s[j] == s[k]:
                    pass
                elif s[j] + s[i] == s[k]:
                    pass
                elif s[j] + s[k] == s[i]:
                    pass
                elif s[k] + s[j] == s[i]:
                    pass
                elif s[k] + s[i] == s[j]:
                    pass
                elif s[i] + s[k] == s[j]:
                    pass
                else:
                    ok = False

                if ok:
                    print("Yes")
                    exit()

    print("No")


if __name__ == "__main__":
    main()
