# -*- coding: utf-8 -*-


def main():
    m, n = map(int, input().split())
    ans = 0

    for i in range(m):
        ans = max(ans, sum(list(map(int, input().split()))))

    print(ans)


if __name__ == '__main__':
    main()
