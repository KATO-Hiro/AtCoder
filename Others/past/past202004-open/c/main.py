# -*- coding: utf-8 -*-


def main():
    n = int(input())
    s = list()
    ans = list()

    for i in range(n):
        si = list(input())
        s.append(si)
        ans.append(si)

    for i in range(n - 1, 0, -1):
        ni = i - 1

        for j in range(1, 2 * n - 1):
            for delta in range(-1, 1 + 1):
                if s[i][j] != "X":
                    continue

                nj = j + delta

                if (nj < 0) or (nj > 2 * n - 2):
                    continue

                if s[ni][nj] != "#":
                    continue

                ans[ni][nj] = "X"

    for a in ans:
        print("".join(map(str, a)))


if __name__ == "__main__":
    main()
