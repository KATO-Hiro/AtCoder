# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    center = (n + 1) // 2
    ans = list()

    if n % 2 == 0:
        # 先頭のみcenter + 残りは降順に
        ans.append(center)

        for value in range(n, 0, -1):
            count = k

            if value == center:
                count -= 1

            for _ in range(count):
                ans.append(value)
    else:
        # 先頭k個はcenter + (center - 1) + 残リは偶数の場合同じ
        for _ in range(k):
            ans.append(center)

        if n >= 3:
            ans.append(center - 1)

            for value in range(n, 0, -1):
                count = k

                if value == center:
                    count = 0
                elif value == center - 1:
                    count -= 1

                for _ in range(count):
                    ans.append(value)

    print(*ans)


if __name__ == "__main__":
    main()
