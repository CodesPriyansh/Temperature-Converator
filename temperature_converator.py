print("Welcome to the Temperature Converator.")
print("You can convert Celsius into Fahrenheit and vice versa.")
choice = input("What you want to convert.")
if choice == "celsius":
    c = int(input("entert the Celsius value:"))
    fahrenheit = 9/5 * c + 32
    print(f"Fahrenheit value: {fahrenheit}")
    
else:
    f = int(input("enter the Fahrenheit value:"))
    celsius = 5/9 * (f - 32)
    print(f"Celsius value: {celsius}")
    

    
    