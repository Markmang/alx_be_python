FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)

def convert_to_celsius(fahrenheit) :
    temperature_celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return temperature_celsius

def convert_to_fahrenheit(celsius) :
    temperature_fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return temperature_fahrenheit

temperature = float(input("Enter the temperature to convert: "))
temperature_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
if temperature_unit == 'C':
    converted_temperature = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is {converted_temperature}°F")
elif temperature_unit == 'F':
    converted_temperature = convert_to_celsius(temperature)
    print(f"{temperature}°F is {converted_temperature}°C")
else:
    print("Invalid temperature. Please enter a numeric value.")
    
