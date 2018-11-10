# -*- coding: utf-8 -*-


def main():
    n, k = map(int, input().split())
    r = sorted(list(map(int, input().split())), reverse=True)
    ans = 0

    for ri in sorted(r[:k]):
        ans = (ans + ri) / 2

    print(ans)


if __name__ == '__main__':
    main()
