def common_elements(x,y):
    a_set=set(x)
    b_set=set(y)
    if len(a_set.intersection(b_set))>0:
        return(a_set.intersection(b_set))
    else:
        return("No common elements")

list1=[]
list2=[]
size_of_list1=int(input("Enter the size of list1: "))
size_of_list2=int(input("Enter the size of list2: "))
for i in range (0,size_of_list1):
    list1.append(int(input("Enter the element in list1: ")))
for i in range (0,size_of_list2):
    list2.append(int(input("Enter the element in list2: ")))
print(f"The common elements are: {common_elements(list1,list2)}")