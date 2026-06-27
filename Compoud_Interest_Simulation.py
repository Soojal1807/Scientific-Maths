
PRINCIPAL = 100
INTEREST_RATE = 0.01
YEAR = 365

def calculate_compound_interest(principal, rate, n):
    return principal * (1 + rate / n) ** n

time_units = {
    "Hours": 24,
    "Minutes": 1440,
    "Seconds": 86400,
    "Milliseconds": 8.64e7,
    "Microseconds": 8.64e10,
    "Nanoseconds": 8.64e13 
}

for unit_name, multiplier in time_units.items():
    total_periods = YEAR * multiplier
    
    result = calculate_compound_interest(PRINCIPAL, INTEREST_RATE, total_periods)
    print(f"Result ({unit_name}): {result}")


"""This is to simulate how our machine hits "Machine Epsilon, """