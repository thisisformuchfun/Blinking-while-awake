# Constants
average_blinks_per_minute = 17.5  # Midpoint of 15 and 20 blinks
duration_of_a_blink_seconds = 0.25  # Midpoint of 100ms (0.1s) and 400ms (0.4s)
average_life_expectancy_years = 72
hours_awake_per_day = 16

# Calculations
seconds_blinking_per_minute = average_blinks_per_minute * duration_of_a_blink_seconds
minutes_in_an_hour = 60
hours_in_a_day = 24

# Time spent blinking per day in seconds
seconds_blinking_per_day = seconds_blinking_per_minute * minutes_in_an_hour * hours_awake_per_day

# Time spent blinking over a lifetime in seconds
seconds_in_a_year = 365.25 * minutes_in_an_hour * hours_in_a_day * 60  # Including leap years
seconds_blinking_over_lifetime = seconds_blinking_per_day * (average_life_expectancy_years * 365.25)

# Convert the lifetime blinking time from seconds to more readable units (days, years)
minutes_blinking_over_lifetime = seconds_blinking_over_lifetime / 60
hours_blinking_over_lifetime = minutes_blinking_over_lifetime / 60
days_blinking_over_lifetime = hours_blinking_over_lifetime / 24
years_blinking_over_lifetime = days_blinking_over_lifetime / 365.25

# Printing results in a command line interface style
print("### Life Spent Blinking Calculator ###\n")
print(f"Average seconds spent blinking per minute: {seconds_blinking_per_minute} seconds")
print(f"Total time spent blinking per day: {seconds_blinking_per_day / 60:.2f} minutes")
print(f"Total years spent blinking in a lifetime: {years_blinking_over_lifetime:.2f} years")

print("\n### Conclusion ###")
print("Over an average lifetime of 72 years, you spend approximately 3.5 years awake with your eyes closed due to blinking.")
