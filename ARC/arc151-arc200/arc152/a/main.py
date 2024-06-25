# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, l = map(int, input().split())
    a = list(map(int, input().split()))

    # 1つ席を空けながら前の組から座る
    # 2人組が座ろうとしたときに、残りの席が1以下ならNo
    for ai in a:
        if ai == 2 and l <= 1:
            print("No")
            exit()

        l -= ai + 1

    print("Yes")


if __name__ == "__main__":
    main()
