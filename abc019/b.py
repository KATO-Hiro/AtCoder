# -*- coding: utf-8 -*-


def main():
    s = input()
    count = 1
    dummy = '0'
    mod_s = s + dummy
    ans = ''

    for i in range(1, len(mod_s)):
        if mod_s[i] == mod_s[i - 1]:
            count += 1
        else:
            ans += mod_s[i - 1] + str(count)
            count = 1

    print(ans)


if __name__ == '__main__':
    main()
