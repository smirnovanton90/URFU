import sys
sys.setrecursionlimit(1000000000)

def multiply_lst(lst):
    if len(lst) == 1: return lst[0]
    return lst[0] * multiply_lst(lst[1:])

def factorial(n):
    if n==0: return 1
    return factorial(n-1)*n


def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    return fib(n-1) + fib(n-2)

print(fib(5))