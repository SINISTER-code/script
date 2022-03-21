def compound_interest(p, r, t):
    A = p * (1 + r / 100) ** t
    Compaound_interest = A - p
    return Compaound_interest
principle = int(input("Enter the principle amount: "))
rate = float(input("Enter the rate: "))
time = int(input("Enter the time: "))
print("Compound interest is: ", compound_interest(principle, rate, time))