print ("Введите размер шоколадки :")
n = int(input())
print ("Х")
m = int(input())
print ("Введите количество долек которые нужно отломить :")
k = int(input())
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('YES')
else:
    print('NO')