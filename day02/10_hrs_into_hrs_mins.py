minutes = float(input("Enter minutes: "))

hours, remainingMinutes = divmod(minutes, 60)

print(f"{round(hours):02}:{round(remainingMinutes):02}")
