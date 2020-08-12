# -*- coding: utf-8 -*-


def main():
    n = int(input())
    st = [0 for _ in range(n)]

    for i in range(n):
        si, ti = map(int, input().split())
        st[i] = (si, ti)

    time = sorted(st, key=lambda x: x[0])
    ans = 1
    last = time[0][1]

    for j in range(1, n):
        last = max(last, time[j - 1][1])

        if last < time[j][0]:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
