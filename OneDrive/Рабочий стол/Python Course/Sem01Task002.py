"""
Задача 2: Найдите сумму цифр трехзначного числа. 
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)
"""
a = 100
print(a // 100 + a % 10 + (a // 10) % 10)