# -*- coding: utf-8 -*-


def main():
    scores = [int(input()) for _ in range(5)]
    total = 0

    for score in scores:
        if score < 40:
            total += 40
        else:
            total += score

    print(total // 5)


if __name__ == '__main__':
    main()
