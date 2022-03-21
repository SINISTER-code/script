def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


n=int(input("Enter the value of n: "))
x=int(input("Enter the value of x: "))
sum = float(0) 
for i in range(0,n+1):
    sum+=float((x**i)/factorial(i))
print((sum))