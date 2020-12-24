# -*- coding: utf-8 -*-


def main():
    s = input()
    n = len(s)
    strings = set()
    strings.add(".")

    for si in s:
        strings.add(si)

    if n >= 2:
        strings.add("..")

        for first, second in zip(s, s[1:]):
            strings.add(first + second)
            strings.add(first + ".")
            strings.add("." + second)

    if n >= 3:
        strings.add("...")

        for first, second, third in zip(s, s[1:], s[2:]):
            strings.add(first + second + third)
            strings.add(first + second + ".")
            strings.add(first + "." + third)
            strings.add("." + second + third)
            strings.add(first + "." + ".")
            strings.add("." + second + ".")
            strings.add("." + "." + third)

    print(len(strings))


if __name__ == "__main__":
    main()
