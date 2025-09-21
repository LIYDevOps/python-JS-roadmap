print("Temperature Converter")
print("="*40)
print("choose an option")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Exit the program")
print("="*40)

history = []

while True:
    try:
        choice = int(input("Enter your choice (1/2/3):"))

        if choice == 1:
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = (celsius * 9/5) + 32
            result = f"{celsius}°C is equal to {fahrenheit}°F"
            print(result)
            history.append(result)
            

        elif choice == 2:
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = (fahrenheit - 32) * 5/9
            result = f"{fahrenheit}°F is equal to {celsius:.2f}°C"
            print(result)
            history.append(result)

        elif choice == 3:
            print("\n Conversion History:")
            if history:

                for i, record in enumerate(history,1):
                    print(f"{i}. {record}")
            else:
                print("No conversions yet.")
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please Enter 1, 2, 3.")
        print("="*40)

    except ValueError:
        print("invalid input. Please enter numeric values only.")
        print("="*40)        

    


