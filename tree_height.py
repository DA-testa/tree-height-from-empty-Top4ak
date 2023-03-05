#221RDB014 Mihails Ruhļa 13. grupa
import sys
from typing import List
import threading

input = sys.stdin.readline

def dfs(v: int, pa: int, path: int, mx: List[int], g: List[List[int]]) -> None:
    mx[v] = path
    for i in g[v]:
        if mx[i] > 0:
            continue
        dfs(i, v, path + 1, mx, g)

def main() -> None:
    mode = input()
    ans = 0
    mx = [0] * 1007
    n = 0
    root = 0
    g = [[] for _ in range(1007)]
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
        n = int(input())
        for i in range(n):
            v = int(input())
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
