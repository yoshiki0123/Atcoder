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
    A = [None] + list(map(int, input().split(' ')))

    ans = 0
    first_sum = 0
    end_id = INF
    for i in range(1, N+1):
        first_sum += A[i]
        if first_sum >= K:
            end_id = i
            ans += N - end_id + 1
            break

    tmp_sum = first_sum
    for j in range(1, N):
        tmp_sum -= A[j]
        if tmp_sum >= K:
            ans += N - end_id + 1
        else:
            if end_id >= N:
                print(ans)
                exit()
            else:
                for k in range(end_id+1, N+1):
                    tmp_sum += A[k]
                    if tmp_sum >= K:
                        end_id = k
                        ans += N - end_id + 1
                        break
                
            if tmp_sum < K:
                print(ans)
                exit()

    print(ans)


if __name__ == '__main__':
    main()



