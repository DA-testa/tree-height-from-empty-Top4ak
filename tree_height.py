#221RDB014 Mihails Ruhļa 13. grupa
import sys
import threading
def compute_height(n, parents):
    tree = {}
    for node, parent in enumerate(parents):
        if parent == -1:
            root = node
        else:
            if parent in tree:
                tree[parent].append(node)
            else:
                tree[parent] = [node]

    stack = [(root, 1)]
    max_height = 1

    while stack:
        node, height = stack.pop()
        max_height = max(max_height, height)
        if node in tree:
            for child in tree[node]:
                stack.append((child, height + 1))

    return max_height

def main():
    mode = input()
    if "F" in mode:
            filename = input()
            if"a" not in filename:
              with open(str("test/"+filename), mode ="r") as f:
                n = int(f.readline())
                parents = list(map(int, f.readline().split()))
            else:
                print("error")
    elif "I" in mode:
            n = int(input())
            parents = list(map(int, input().split()))
    else:
           print("invalid mode.")
    print(compute_height(n, parents))
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
