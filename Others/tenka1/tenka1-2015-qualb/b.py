# -*- coding: utf-8 -*-


def main():
    s = input()

    if s == "{}":
        print('dict')
        exit()

    count = 0
    ans = 'set'

    # See:
    # https://tenka1.klab.jp/2015/explain/qualb_b.html
    # なぜ、":"が含まれているかどうかだけで判定してはいけないのかがわかっていない
    for si in s:
        if si == "{":
            count += 1
        elif si == "}":
            count -= 1
        elif count == 1 and si == ':':
            ans = 'dict'
            break

    print(ans)


if __name__ == '__main__':
    main()
