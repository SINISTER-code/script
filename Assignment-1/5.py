def leap_year(start,end):
    leap_year=[]
    for i in range(start,end+1):
        if i%4==0 and i%100!=0 or i%400==0:
            leap_year.append(i)
    return leap_year
start=int(input("Enter the start value: "))
end=int(input("Enter the end value: "))
print(leap_year(start,end))