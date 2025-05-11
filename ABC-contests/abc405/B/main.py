#library
import sys, re, heapq
from math import ceil, floor, sqrt, isqrt, pi, gcd, comb
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations, product

sys.setrecursionlimit(10**6)
INF = float('inf')

#class

#def

#main
def main():
    N, M = map(int,input().split())
    A = list(map(int, input().split(' ')))
    que = deque(A)
    
    for ans in range(N + 1):
        s = set(que)
        if not all(i in s for i in range(1, M + 1)):
            print(ans)
            return
        if que:
            que.pop()
                    

if __name__ == '__main__':
    main()