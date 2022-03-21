import  random
list=[]
even=[]
for i in range(100,901):
    if i%2==0:
        list.append(i)
random.shuffle(list)
for i in range (0,100):
    even.append(list[i])
print(f"the number of elements in the list are: {len(even)}")
a=input("And if you want to print the elements of the list enter Y or N ")
if a=="Y" or a=="y":
    print(even)
else:
    print("Thank you")