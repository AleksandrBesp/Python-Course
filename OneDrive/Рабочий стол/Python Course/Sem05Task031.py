"""Задача №31. Решение в группах
Последовательностью Фибоначчи называется
последовательность чисел a0, a1, ..., an, ..., 
где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи
Input: 7
Output: 21
Задание необходимо решать через рекурсию
"""
def Fibonacci(n):
    if n in [1,2]:  # if n < 3 :
        return n
    return Fibonacci(n-1) + Fibonacci(n-2)
n = 7

print(Fibonacci(n))


fib1, fib2 = 0, 1
for i in range(0, n):
    fib1, fib2 = fib2, fib2 + fib1
print(fib2)
