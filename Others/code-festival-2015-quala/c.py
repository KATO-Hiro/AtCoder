# -*- coding: utf-8 -*-


def main():
    n, t = map(int, input().split())
    ans = n
    remain = t
    diff = [0 for _ in range(n)]

    for i in range(n):
        ai, bi = map(int, input().split())
        remain -= bi
        diff[i] = ai - bi

    if remain < 0:
        print(-1)
    else:
        for d in sorted(diff):
            remain -= d

            if remain >= 0:
                ans -= 1
            else:
                print(ans)
                exit()

        print(ans)


if __name__ == '__main__':
    main()
