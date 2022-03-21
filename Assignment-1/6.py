salery = int(input("Enter Salery:"))
if salery <=  10000:
  hra = (salery * 20) /100
  da = (salery * 80) /100
elif salery <= 20000:
  hra = (salery * 25) /100
  da = (salery * 90) /100
else:
  hra = (salery * 30) /100
  da = (salery * 95) /100

gross_salary = salery + da + hra
print(gross_salary)