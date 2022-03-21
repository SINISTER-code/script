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

prime=prime(100,900)
random.shuffle(prime)
list=[]
for i in range(0,100):
    list.append(prime[i])

print(f"the number of elements in the list are: {len(list)}")
a=input("And if you want to print the elements of the list enter Y or N ")
if a=="Y" or a=="y":
    print(list)
else:
    print("Thank you")

