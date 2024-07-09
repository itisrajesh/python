# Write a program WindChill.java that takes two double command-line arguments t
# and v and prints the wind chill. Use Math.pow(a, b) to compute ab. Given the
# temperature t (in Fahrenheit) and the wind speed v (in miles per hour), the
# National Weather Service defines the effective temperature (the wind chill) to be:

# Note: the formula is not valid if t is larger than 50 in absolute value or if v is larger
# than 120 or less than 3 (you may assume that the values you get are in that range).


import sys


temperature_entered = sys.argv[1] 
wind_speed_entered = sys.argv[2]

temperature = None
wind_speed = None

if temperature_entered.isdecimal() or temperature_entered.isdigit():
    temperature = float(temperature_entered)

if wind_speed_entered.isdecimal() or wind_speed_entered.isdigit():
    wind_speed = float(wind_speed_entered)

if temperature is None:
    print(f"Invalid input {temperature_entered}. Enter Valid Temperature")
elif wind_speed is None:
    print(f"Invalid input {wind_speed_entered}. Enter Valid Wind Speed")
elif abs(temperature) > 50 or wind_speed > 120 or wind_speed < 3:
    print(f"Invalid input. Temperature {temperature} must be between -50 and 50 °F",
            f"and wind speed {wind_speed} between 3 and 120 mph.")
else :
    wind_chill = 35.74 + 0.6215 * temperature - 35.75 * (wind_speed ** 0.16) + 0.4275 * temperature * (wind_speed ** 0.16)
    print(f"Wind Chill: {wind_chill:.2f} °F for temperature {temperature} and wind speed {wind_speed}")
