# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ans = list()

    for i in range(n + 1):
        ok = False

        for j in range(1, 10):
            if (i * j) % n == 0:
                ans.append(str(j))
                ok = True
                break

        if not ok:
            ans.append("-")

    print("".join(ans))


if __name__ == "__main__":
    main()
