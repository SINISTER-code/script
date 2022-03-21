import  random
list=[]
odd=[]
for i in range(100,901):
    if i%2!=0:
        list.append(i)
random.shuffle(list)
for i in range (0,100):
    odd.append(list[i])
print(f"the number of elements in the list are: {len(odd)}")
a=input("And if you want to print the elements of the list enter Y or N ")
if a=="Y" or a=="y":
    print(odd)
else:
    print("Thank you")