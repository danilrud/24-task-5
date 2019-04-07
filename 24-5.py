N = int(input())
summa = 0
while N > 0:
    d = N % 10
    N = N // 10
    summa += d
print(summa)
