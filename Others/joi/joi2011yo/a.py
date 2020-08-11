# -*- coding: utf-8 -*-


def main():
    seconds = sum([int(input()) for _ in range(4)])
    minute, second = divmod(seconds, 60)
    print(minute)
    print(second)


if __name__ == '__main__':
    main()
