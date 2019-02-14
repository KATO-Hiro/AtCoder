# -*- coding: utf-8 -*-


def main():
    n, k = map(int, input().split())
    ts = [list(map(int, input().split())) for _ in range(n)]

    # See:
    # https://www.slideshare.net/chokudai/abc015
    def dfs(questionnaire_count, value):
        if questionnaire_count == n:
            return value == 0

        for i in range(k):
            if dfs(questionnaire_count + 1, value ^ ts[questionnaire_count][i]):
                return True

        return False

    if dfs(0, 0):
        print('Found')
    else:
        print('Nothing')


if __name__ == '__main__':
    main()
