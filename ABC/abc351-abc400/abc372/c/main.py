# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())
    s = ["?"] * 2 + list(input().rstrip()) + ["?"] * 2
    base = 0

    # 初回のみ全探索 + 差分更新
    for i in range(2, n):
        if i + 2 > n + 1:
            continue

        si = s[i] + s[i + 1] + s[i + 2]
        # print(si)

        if si == "ABC":
            base += 1

    # print(base)
    ans = [base]

    def f(xi):
        count = 0

        for i in range(xi - 2, xi + 1):
            t = ""

            for j in range(i, i + 3):
                t += s[j]

                if t == "ABC":
                    count += 1

        return count

    for _ in range(q):
        xi, ci = input().rstrip().split()
        xi = int(xi) + 1

        before = f(xi)
        s[xi] = ci
        after = f(xi)
        diff = after - before
        ans.append(ans[-1] + diff)

    print(*ans[1:], sep="\n")


if __name__ == "__main__":
    main()
