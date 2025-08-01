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
def base_10(num_n, n):
    """
    n 進数で表された整数を 10 進数に変換する。

    Parameters:
        num_n (int | str): n 進数で表された数（各桁は 0 ≦ d < n）。
        n (int): 基数。

    Returns:
        int: 10 進数に変換した結果。
    """
    num_10 = 0
    for s in str(num_n):
        num_10 *= n
        num_10 += int(s)
    return num_10


#main
def main():
    K = int(input())
    A, B = map(int,input().split())

    print(base_10(A, K) * base_10(B, K))
    
    

if __name__ == '__main__':
    main()