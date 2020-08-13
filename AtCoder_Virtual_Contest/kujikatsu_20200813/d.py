# -*- coding: utf-8 -*-


from itertools import groupby


def runLengthEncode(S: str):
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, str(len(list(v)))))
    return res


def main():
    s = input()
    length = len(s)
    s_count = 0

    # See:
    # https://qiita.com/Kept1994/items/e9179d1dd7c6455d6883
    runLength = runLengthEncode(s)

    for first, second in zip(runLength, runLength[1:]):
        if first[0] == 'S' and second[0] == 'T':
            first_count = int(first[1]) + s_count
            second_count = int(second[1])

            if first_count > second_count:
                s_count = first_count - second_count
            else:
                s_count = 0

            length -= 2 * min(first_count, second_count)

    print(length)


if __name__ == '__main__':
    main()
