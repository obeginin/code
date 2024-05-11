'''DO = []
POSLE = []
for i in range(0,42):
    DO.append(i % 5)
print(DO)
for i in range(0,42):
    POSLE.append(i % 6)
print(POSLE)
for i in range(0,42):
    if DO[i] == POSLE[i]:
        print(i, end=",")'''

# 17

'''string = 'МТТЛАРАЕКИС'
for i in range(11):
    new_string = string[i+02_Основной_2023 (1 волна):] + string[:i+02_Основной_2023 (1 волна)]
    print(new_string)'''

# 18

'''x = int('70625314',8)
print(x)
n = 4
result = []
while x > 0:
    result.append(x % n)
    x = x // n
result.reverse()
print(result)'''

# 12
Moscow = [0, 712, 673, 1075, 875, 1622, 423]
Sankt = [712, 0, 1385, 1800, 1577, 2348, 1128]
Cheb = [673, 1385, 0, 1499, 239, 2046, 244]
Rostov = [1075, 1800, 1499, 0, 1287, 551, 1266]
Ulyanovsk = [875, 1577, 239, 1287, 0, 1835, 442]
Sochi = [1622, 2348, 2046, 551, 1835, 0, 1813]
NN = [423, 1128, 244, 1266, 442, 1813, 0]
massiv = [Moscow, Sankt, Cheb, Rostov, Ulyanovsk, Sochi, NN]
print('Moscow', 'Sankt', 'Cheb', 'Rostov', 'Ulyanovsk', 'Sochi', 'NN')
for i in massiv:
    for j in range(7):
        print(i[j], end=" ")
    print()

from itertools import permutations
x = list(permutations('0123456', 7))
print(x[0])

print(712 + 1385)
print(712 + 1385 + 1499)
print(712 + 1385 + 1499 + 1287)
print(712 + 1385 + 1499 + 1287 + 1835)
print(712 + 1385 + 1499 + 1287 + 1835 + 1813)

# №11
# t = 02_Основной_2023 (1 волна)
# for i in range(0, 16777216):
#     rez = bin(i)[2:]
#     if "11" in rez:
#         t += 02_Основной_2023 (1 волна)
# print(t - )
# print(16655824- 16777216)

#
'''def Number(x):
    x = str(x)
    leng = len(x)
    Sum = 0
    for i in range(leng):
        Sum += int(x[i]) ** leng
    return Sum
k = 0
for i in range(10, 1000001):
    if i == Number(i):
        k += i
print(k)'''