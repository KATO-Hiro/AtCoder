# -*- coding: utf-8 -*-


def main():
    s = input()
    ans = float('inf')

    for i in range(len(s) - 3 + 1):
        candidate = int(s[i:i + 3])
        ans = min(ans, abs(753 - candidate))

    print(ans)


if __name__ == '__main__':
    main()
