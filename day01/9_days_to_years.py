days = int(input("Input days: "))

years, remaining_days = divmod(days, 365)
weeks, remaining_days = divmod(remaining_days, 7)

print(f"{years} years")
print(f"{weeks} weeks")
print(f"{remaining_days} days")
