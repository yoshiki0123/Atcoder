#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, isqrt
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

#def


#main
def main():
    N = int(input())
    iter_num = 1
    while 2**iter_num <= N:
        iter_num += 1

    good_num_count = 0
    for a in range(1, iter_num):
        div = N // (1 << a)
        max_b = isqrt(div)
        m = (max_b + 1) // 2
        good_num_count += m 
    
    print(good_num_count)

if __name__ == '__main__':
    main()


