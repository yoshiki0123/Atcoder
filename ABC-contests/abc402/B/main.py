#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

#def

#main
def main():
    Q = int(input())
    que = deque()
    
    for _ in range(Q):
        query = input().split()
        if query[0] == '1':
            _, x = query
            x = int(x)
            que.append(x)
    
        elif query[0] == '2':
            print(que.popleft())

        
if __name__ == '__main__':
    main()