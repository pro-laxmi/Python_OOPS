n = int(input())
sum = 0
d = 0
k = n
while k:
    d = d+1
    k = k//10
for i in range(1,n+1):
    sum = sum | i
print(sum * d)
