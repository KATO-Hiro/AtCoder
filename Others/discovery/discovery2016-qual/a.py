# -*- coding: utf-8 -*-


def main():
    text = 'DiscoPresentsDiscoveryChannelProgrammingContest2016'
    w = int(input())

    while len(text) > 0:
        print(text[:w])
        text = text[w:]


if __name__ == '__main__':
    main()
