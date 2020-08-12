# -*- coding: utf-8 -*-


def main():
    numbers = [str(i) for i in range(1, 1000 + 1)]
    print('\n'.join(map(str, sorted(numbers))))


if __name__ == '__main__':
    main()
