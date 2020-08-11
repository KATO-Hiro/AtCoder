# -*- coding: utf-8 -*-


def main():
    alpha = sorted(list(map(int, input().split())), reverse=True)
    print(alpha[2])


if __name__ == '__main__':
    main()
