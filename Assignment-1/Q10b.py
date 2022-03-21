from Q10a import *
principle = int(input("Enter the principle amount: "))
rate = float(input("Enter the rate: "))
time = int(input("Enter the time: "))
print("Compound interest is: ", compound_interest(principle, rate, time))