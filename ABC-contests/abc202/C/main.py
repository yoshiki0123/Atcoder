#library
import sys, re, heapq
from math import sin, cos, radians, ceil, floor, sqrt, isqrt, pi, gcd, comb
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations, product

sys.setrecursionlimit(10**6)
INF = float('inf')

#class

#def

#main
def main():
    N = int(input())
    A = list(map(int, input().split(' ')))
    B = list(map(int, input().split(' ')))
    C = list(map(int, input().split(' ')))

    A_value_count = Counter(A)
    B_value_indexs = defaultdict(list)
    C_index_count = Counter(C)
    
    for i in range(N): 
        B_value_indexs[B[i]].append(i)

    ans = 0
    for value, indexs in B_value_indexs.items():
        for index in indexs:
            ans += A_value_count.get(value, 0) * C_index_count.get(index+1, 0)
    
    print(ans)

if __name__ == '__main__':
    main()