# -*- coding: utf-8 -*-


def main():
    s = input()
    ans = 0
    j = 0

    for i in range(len(s)):
        if ord(s[i]) <= ord(s[j]):
            j = i
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
