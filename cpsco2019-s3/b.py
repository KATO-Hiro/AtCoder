# -*- coding: utf-8 -*-


def main():
    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())), reverse=True)
    ans = 1

    for ai in a:
        m -= ai

        if m <= 0:
            print(ans)
            exit()

        ans += 1


if __name__ == '__main__':
    main()
