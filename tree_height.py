#221RDB014 Mihails Ruhļa 13. grupa
import sys
from typing import List, Tuple
import threading

input = sys.stdin.readline

ll = int
ld = float
pt = Tuple[ll, ll]

def dfs(v: ll, pa: ll, path: ll, mx: List[ll], g: List[List[ll]]) -> None:
    mx[v] = path
    for i in g[v]:
        if mx[i] > 0:
            continue
        dfs(i, v, path + 1, mx, g)

def main() -> None:
    mode = input()
    ans = 0
    mx = [0] * 107
    n = 0
    root = 0
    g = [[] for _ in range(107)]
    if "F" in mode:
        filename = input()
        if"a" not in filename:
            with open(str("test/"+filename), mode ="r") as f:
                n = int(f.readline())
                parents = list(map(int, f.readline().split()))
                for i, j in enumerate(parents):
                    if j == -1:
                        root = i
                        continue
                    g[i].append(j)
                    g[j].append(i)
    else:
        n = ll(input())
        for i in range(n):
            v = ll(input())
            if v == -1:
                root = i
                continue
            g[v].append(i)
            g[i].append(v)

    dfs(root, -1, 1, mx, g)

    for i in range(n):
        ans = max(ans, mx[i])

    print(ans)

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
