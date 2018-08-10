# -*- coding: utf-8 -*-


def main():
    s = input()
    words = {'Left': '<', 'Right': '>', 'AtCoder': 'A'}

    # See:
    # https://www.slideshare.net/chokudai/arc045
    for key, value in words.items():
        s = s.replace(key, value)

    print(s)


if __name__ == '__main__':
    main()
