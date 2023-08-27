n = int(input())
custo=[]
i=1
b=0
custof=[]
y=0
while i<=n:
    x=float(input())
    custo.append(x)
    total = sum(custo)
    i=i+1
    divisao=total/n
for e in range(0,n):
    if custo[e]<divisao:
        b = b + 1
for y in range(0,n):
    if custo[y]<divisao:
        a = divisao - custo[y]
        custof.append(a)
custoff = sum(custof)



print(custoff)