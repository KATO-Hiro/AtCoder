# -*- coding: utf-8 -*-


def main():
    n = int(input())
    cs = [input() for _ in range(n)]
    count1 = 0
    count2 = 0
    ans = 0

    for ci in cs:
        if ci == '/':
            if count2 == 0:
                count1 += 1
            else:
                if count1 == count2:
                    ans += 1

                count1 = 1
                count2 = 0
        elif ci == '\\' and count1 >= 1:
            count2 += 1
    else:
        if count1 == count2:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
