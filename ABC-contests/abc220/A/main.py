#library
import sys, re, heapq
from math import (
sin, cos, radians, ceil, 
floor, sqrt, isqrt, pi, 
gcd, comb, factorial
)
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
    A, B, C = map(int,input().split())
    for i in range(A, B+1):
        if i % C == 0:
            print(i)
            exit()
    
    print(-1)

    

if __name__ == '__main__':
    main()