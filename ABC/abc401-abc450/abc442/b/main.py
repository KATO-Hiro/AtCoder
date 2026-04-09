# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    q = int(input())
    volume = 0
    is_stopped = True

    for _ in range(q):
        ai = int(input())

        if ai == 1:
            volume += 1
        elif ai == 2:
            if volume >= 1:
                volume -= 1
        else:
            is_stopped = not is_stopped

        if not is_stopped and volume >= 3:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
