principal_amount = float(input("Enter principal amount: "))
interest_rate = float(input("Enter interest rate: "))
time_period = float(input("Enter time period: "))

amount = principal_amount * (pow((1 + interest_rate / 100), time_period))

compound_interest = amount - principal_amount

print(f"Compound interest: {compound_interest}")
