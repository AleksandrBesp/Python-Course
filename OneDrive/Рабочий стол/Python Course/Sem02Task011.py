# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6
#  1 вариант
num = int(input('Введите число: '))

if num <= 1:
    print(-1)
else:
    fib_curr, fib_next = 0, 1
    n = 2
    while fib_next <= num:
        if fib_next == num:
            print(n)
            break
        fib_curr, fib_next = fib_next, fib_curr + fib_next
        n += 1
    else:
        print(-1)

# 2 вариант

n = 4
summ = 0
f_1 = 1
f_2 = 1
num = 3

while summ < n:
    summ = f_1 + f_2
    f_1 = f_2
    f_2 = summ
    num += 1
print(f'{num}' if summ == n else '-1')