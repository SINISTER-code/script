L=[]
Number_of_elements_in_list=int(input("Enter the number of elements in the list: "))
for i in range (0,Number_of_elements_in_list):
    L.append(int(input("Enter the element in the list: ")))
print("How many elements you want to add in the list: ")
Number_of_elements_to_add=int(input())
for i in range (0,Number_of_elements_to_add):
    L.append(int(input("Enter the element in the list: ")))
print(L)