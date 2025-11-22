FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

temperature_input = float(input("Enter the temperature to convert: "))

unit_input = input("Is this temperature in Fahrenheit or Celsius? (F/C): ").strip().upper()

if unit_input == 'F':
    converted_temperature = convert_to_celsius(temperature_input)
    print(f"{temperature_input}°F is {converted_temperature}°C")
elif unit_input == 'C':
    converted_temperature = convert_to_fahrenheit(temperature_input)
    print(f"{temperature_input}°C is {converted_temperature}°F")
else:
    print("Invalid unit. Please enter 'F' for Fahrenheit or 'C' for Celsius.")