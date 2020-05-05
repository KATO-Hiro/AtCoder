# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    score = sorted(map(int, input().split()), reverse=True)
    print(sum(score[:2]))


if __name__ == '__main__':
    main()
