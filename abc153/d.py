# -*- coding: utf-8 -*-

def main():
    n = int(input())
    j = 0
    count = 1

    while n > 1:
        n //= 2
        j += 1
        count += 2 ** j

    print(count)


if __name__ == '__main__':
    main()
