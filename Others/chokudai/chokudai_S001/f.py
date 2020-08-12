# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 1

    if n == 1:
        print(ans)
        exit()

    tmp = a[0]

    for ai in a[1:]:
        if ai > tmp:
            tmp = ai
            ans += 1

    print(ans)



if __name__ == '__main__':
    main()
