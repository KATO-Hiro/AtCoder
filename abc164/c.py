# -*- coding: utf-8 -*-


def main():
    n = int(input())
    ans = set()

    for i in range(n):
        si = input()
        ans.add(si)

    print(len(ans))


if __name__ == '__main__':
    main()
