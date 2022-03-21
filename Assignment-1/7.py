# Method-1

# # import re
# # password=input("Enter the password: ")
# # flag=0
# # while True:
# #     if (len(password))<8:
# #         flag=1
# #         break
# #     elif not re.search("[a-z]",password):
# #         flag=1
# #         break
# #     elif not re.search("[A-Z]",password):
# #         flag=1
# #         break
# #     elif not re.search("[0-9]",password):
# #         flag=1
# #         break
# #     elif not re.search("[_^$#@]",password):
# #         flag=1
# #         break
# #     else:
# #         flag=0
# #         break
# # if flag==1:
# #     print("Password is not valid")
# # else:
# #     print("Password is valid")


# # Method-2
password=input("Enter the password: ")
l=0
u=0
d=0
s=0
if (len(password)>=8):
    for i in password:
        if (i.islower()):
            l+=1
        elif (i.isupper()):
            u+=1
        elif (i.isdigit()):
            d+=1
        elif (i=="_" or i=="^" or i=="$" or i=="#" or i=="@"):
            s+=1
    if (l>=1 and u>=1 and d>=1 and s>=1):
        print("Password is valid")
    else:
        print("Password is not valid")
