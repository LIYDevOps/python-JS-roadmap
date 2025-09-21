print("Temperature Converter")
print("-"*40)
print("choose an option")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Exit the program")
print("-"*40)

while True:
    choice = int(input("Enter your choice (1/2/3):"))

    if choice == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is equal to {fahrenheit}°F")
    elif choice == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
    elif choice == 3:
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
