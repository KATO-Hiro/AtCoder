# -*- coding: utf-8 -*-


def main():
    n, m = list(map(int, input().split()))
    a = [int(input()) for _ in range(m)]
    threads = dict()
    used_thread = [False for _ in range(n)]

    for index, ai in enumerate(a, 1):
        threads[ai] = index

    for thread_number, order in sorted(threads.items(), key=lambda x: x[1], reverse=True):
        used_thread[thread_number - 1] = True
        print(thread_number)

    for index, is_used in enumerate(used_thread, 1):
        if not is_used:
            print(index)


if __name__ == '__main__':
    main()
