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
    R, X = map(int,input().split())

    if X == 1:
        if 1600 <= R and R <= 2999:
            print("Yes")
        else:
            print("No")
    else:
        if 1200 <= R and R <= 2399:
            print("Yes")
        else:
            print("No")

    

if __name__ == '__main__':
    main()