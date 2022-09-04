# -*- coding: utf-8 -*-


import heapq
 

# See:
# https://atcoder.jp/contests/abc267/submissions/34540677
class Heapq:
    def __init__(self, hq = [], descending_order = False):
        if descending_order:
            self.sign = -1
            self.hq = [-l for l in hq]
        else:
            self.sign = 1
            self.hq = hq[:]

        heapq.heapify(self.hq)
        self.total = sum(hq)
        self.count = {}

        for l in hq:
            self.count[l] = self.count.get(l, 0) + 1

        self.length = len(hq)
    
    def __bool__(self):
        return self.length > 0
        
    def __len__(self):
        return self.length
    
    def __getitem__(self, i):
        if i == 0:
            return self.top()
        else:
            assert False
    
    def push(self, x):
        self.length += 1
        self.count[x * self.sign] = self.count.get(x * self.sign, 0) + 1
        heapq.heappush(self.hq, x * self.sign)
        self.total += x
    
    def pop(self):
        if self.length == 0:
            return None

        self.length -= 1
        result = heapq.heappop(self.hq)
        self.total -= self.sign * result
        self.count[result] -= 1
        self.delete()

        return self.sign * result
    
    def top(self):
        if self.hq:
            return self.sign * self.hq[0]
        else:
            return None
    
    def remove(self, x):
        if self.count.get(x * self.sign, 0) == 0:
            return False

        self.count[x * self.sign] -= 1
        self.length -= 1
        self.total -= x
        self.delete()

        return True
            
    def delete(self):
        while self.hq and self.count.get(self.hq[0], 0) == 0:
            heapq.heappop(self.hq)


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    graph = [[] for _ in range(n)]
    
    for _ in range(m):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1
    
        graph[ai].append(bi)
        graph[bi].append(ai)

    costs = [0] * n
    hq = Heapq()

    for i in range(n):
        for to in graph[i]:
            costs[i] += a[to]
    
    # コストをheapで管理
    # インデックスも含めている
    for i, cost in enumerate(costs):
        hq.push(cost * n + i)
    
    used = [False] * n
    ans = 0

    while hq:
        cost, v = divmod(hq.pop(), n)

        used[v] = True
        ans = max(ans, cost)

        for to in graph[v]:
            if used[to]:
                continue
    
            hq.remove(costs[to] * n + to)
            costs[to] -= a[v]
            hq.push(costs[to] * n + to)

    print(ans)


if __name__ == "__main__":
    main()
