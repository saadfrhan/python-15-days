first_name = input("Enter your firstname: ")
last_name = input("Enter your lastname: ")
print(f"{first_name} {last_name}")

temp = first_name
first_name = last_name
last_name = temp
print("Value swapped")

print(f"{first_name} {last_name}")
