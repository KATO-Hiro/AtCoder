# -*- coding: utf-8 -*-


def main():
    n, x = map(int, input().split())

    # See:
    # https://www.youtube.com/watch?v=VX8cGy7kNTE
    if (x == 1) or (x == (2 * n - 1)):
        print('No')
    else:
        print('Yes')

        numbers = [i for i in range(1, 2 * n - 1 + 1)
                   if (i < x - 1) or (x + 1 < i)]
        half = n - 2

        for ans in numbers[:half] + [x - 1, x, x + 1] + numbers[half:]:
            print(ans)


if __name__ == '__main__':
    main()
