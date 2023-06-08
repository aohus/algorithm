"""
link : https://leetcode.com/problems/climbing-stairs/
"""


#
def cs(n):
    pass


# top-down(memorization) 방식

memo = {}


def cs_topdown(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n not in memo:
        memo[n] = cs_topdown(n - 1) + cs_topdown(n - 2)
    return memo[n]


# bottom-up(tabulation, dp table) 방식
memo = {1: 1, 2: 2}


def cs_bottomup(n):
    for i in range(3, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo[n]
