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
    N, K = map(int,input().split())
    A = list(map(int, input().split(' ')))
    
    right = 0
    sum = 0
    ans = 0

    for left in range(N):
        while right < N and sum + A[right] < K:
            sum += A[right]
            right += 1
        
        ans += N - right
        sum -= A[left]
    
    print(ans)
    

if __name__ == '__main__':
    main()