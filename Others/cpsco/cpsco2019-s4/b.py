# -*- coding: utf-8 -*-


def main():
    n, d = map(int, input().split())
    s = [input() for _ in range(d)]
    ans = 0

    for i in range(d):
        for j in range(i, d):
            if i != j:
                count = 0

                for si, sj in zip(s[i], s[j]):
                    if si == 'o' or sj == 'o':
                        count += 1

                ans = max(ans, count)

    print(ans)


if __name__ == '__main__':
    main()
