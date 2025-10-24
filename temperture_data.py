# Weekly Temperature Input

temperatures_data.csv= []

print("Enter daily temperatures for the week (in degrees):")
for day in range(7):
    while True:
        try:
            temp = float(input(f"Day {day + 1} temperature: "))
            temperatures.append(temp)
            break
        except ValueError:
            print("Please enter a valid number.")

print(f"\nWeekly temperatures: {temperatures}")
print(f"Average temperature: {sum(temperatures) / len(temperatures):.1f}°")
print(f"Highest temperature: {max(temperatures)}°")
print(f"Lowest temperature: {min(temperatures)}°")