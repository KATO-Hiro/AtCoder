# -*- coding: utf-8 -*-


def main():
    n = int(input())
    s = input()
    ans = 'Yes'
    prev = s[0]
    fianl = s[-1]
    r_count = 0
    g_count = 0
    b_count = 0

    if prev != 'R' or fianl != 'B':
        print('No')
        exit()
    else:
        r_count += 1

    for i in range(1, n):
        cur = s[i]

        if prev == 'R':
            if cur == 'R':
                r_count += 1
            elif cur == 'G':
                g_count += 1
            else:
                print('No')
                exit()
        elif prev == 'G':
            if cur == 'G':
                print('No')
                exit()
            elif cur == 'R':
                if r_count == 0:
                    print('No')
                    exit()

                r_count += 1
            elif cur == 'B':
                b_count += 1
        elif prev == 'B':
            if cur == 'B':
                if r_count == 0:
                    print('No')
                    exit()

                b_count += 1
            elif cur == 'R':
                r_count = 1
                g_count = 0
                b_count = 0
            elif cur == 'G':
                if g_count > 0:
                    g_count += 1
                else:
                    print('No')
                    exit()

        prev = cur

    print(ans)


if __name__ == '__main__':
    main()
