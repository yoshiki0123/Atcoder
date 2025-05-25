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
    N, K = map(int,input().split())
    ans = 0
    for i in range(1, N+1):
        for j in range(1, K+1):
            room_num_str = str(i) + '0' + str(j)
            room_num = int(room_num_str)
            ans += room_num
    
    print(ans)

    

if __name__ == '__main__':
    main()