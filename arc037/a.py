# -*- coding: utf-8 -*-


def main():
    n = int(input())
    m = list(map(int, input().split()))
    study_hours = 0

    for mi in m:
        if mi < 80:
            study_hours += 80 - mi

    print(study_hours)


if __name__ == '__main__':
    main()
