# -*- coding: utf-8 -*-


def main():
    n, k = map(int, input().split())
    h = sorted(list(map(int, input().split())), reverse=True)
    count = 0
    ans = 0

    for hi in h:
        if count >= k:
            ans += hi

        count += 1

    print(ans)


if __name__ == '__main__':
    main()
