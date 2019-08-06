# -*- coding: utf-8 -*-


def main():
    n, m = map(int, input().split())
    places = [list(map(int, input().split())) for _ in range(n)]
    d = dict()

    for j in range(m):
        count = 0

        for i in range(n):
            if places[i][j] == 1:
                count += 1

        d[j + 1] = count

    ans = ''

    for key, value in sorted(d.items(), key=lambda x: x[1], reverse=True):
        ans += str(key)

    print(' '.join(map(str, list(ans))))


if __name__ == '__main__':
    main()
