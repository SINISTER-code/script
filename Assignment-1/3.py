import random
def prime(start, end):
    prime=[]
    for i in range(start, end+1):
        if i==0 or i==1:
            continue
        else:
            for j in range(2,int(i/2)+1):
                if i%j==0:
                    break
            else:
                prime.append(i)
    return prime
start=int(input("Enter the start value: "))
end=int(input("Enter the end value: "))
print(prime(start,end))