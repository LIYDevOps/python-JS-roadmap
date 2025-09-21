#initializing the variables

choice = input("Type C to convert from Celsius to Fahrenheit and F to convert from Fahrenheit to Celsius:")

#taking input from the user
if choice.upper() == "C":
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is equal to {fahrenheit}°F")
elif choice.upper() == "F":
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
else:
    print("Invalid choice! Please enter C or F.")
