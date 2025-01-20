# -*- coding: utf-8 -*-


class Deque:
    def __init__(self, src_arr=[], max_size=300000):
        self.N = max(max_size, len(src_arr)) + 1
        self.buf = list(src_arr) + [None] * (self.N - len(src_arr))
        self.head = 0
        self.tail = len(src_arr)

    def __index(self, i):
        l = len(self)
        if not -l <= i < l:
            raise IndexError("index out of range: " + str(i))
        if i < 0:
            i += l
        return (self.head + i) % self.N

    def __extend(self):
        ex = self.N - 1
        self.buf[self.tail + 1 : self.tail + 1] = [None] * ex
        self.N = len(self.buf)
        if self.head > 0:
            self.head += ex

    def is_full(self):
        return len(self) >= self.N - 1

    def is_empty(self):
        return len(self) == 0

    def append(self, x):
        if self.is_full():
            self.__extend()
        self.buf[self.tail] = x
        self.tail += 1
        self.tail %= self.N

    def appendleft(self, x):
        if self.is_full():
            self.__extend()
        self.buf[(self.head - 1) % self.N] = x
        self.head -= 1
        self.head %= self.N

    def pop(self):
        if self.is_empty():
            raise IndexError("pop() when buffer is empty")
        ret = self.buf[(self.tail - 1) % self.N]
        self.tail -= 1
        self.tail %= self.N
        return ret

    def popleft(self):
        if self.is_empty():
            raise IndexError("popleft() when buffer is empty")
        ret = self.buf[self.head]
        self.head += 1
        self.head %= self.N
        return ret

    def __len__(self):
        return (self.tail - self.head) % self.N

    def __getitem__(self, key):
        return self.buf[self.__index(key)]

    def __setitem__(self, key, value):
        self.buf[self.__index(key)] = value

    def __str__(self):
        return "Deque({0})".format(str(list(self)))


def main():
    import sys

    input = sys.stdin.readline

    q = int(input())
    d = Deque([], max_size=300100)
    minus = 0

    for _ in range(q):
        qi = list(map(int, input().split()))

        if qi[0] == 1:
            l = qi[1]

            if len(d) == 0:
                d.append((l, l))
                minus = 0
            else:
                d.append((l, l + d[-1][1]))
        elif qi[0] == 2:
            li, _ = d.popleft()
            minus += li
        else:
            k = qi[1]
            k -= 1
            print(d[k][1] - d[k][0] - minus)


if __name__ == "__main__":
    main()
