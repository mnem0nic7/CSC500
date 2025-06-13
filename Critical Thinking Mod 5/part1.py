def main():
    total_rainfall = 0.0
    total_months = 0

    years = int(input("Enter the number of years: "))

    for year in range(1, years + 1):
        print(f"\nYear {year}:")
        for month in range(1, 13):
            while True:
                try:
                    rainfall = float(input(f"  Enter the inches of rainfall for month {month}: "))
                    if rainfall < 0:
                        print("    Rainfall cannot be negative. Please enter a valid amount.")
                        continue
                    break
                except ValueError:
                    print("    Invalid input. Please enter a number.")
            total_rainfall += rainfall
            total_months += 1

    average_rainfall = total_rainfall / total_months if total_months else 0

    print("\nRainfall Statistics")
    print(f"Total months: {total_months}")
    print(f"Total inches of rainfall: {total_rainfall:.2f}")
    print(f"Average rainfall per month: {average_rainfall:.2f}")

if __name__ == "__main__":
    main()