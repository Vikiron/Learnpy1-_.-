# Import necessary libraries
import pandas as pd
from datetime import datetime

# Get the current date and time
current_date = datetime.now()

# Convert the current date to a Pandas Timestamp
current_date_timestamp = pd.Timestamp(current_date)

# Create a Timestamp for the start of the current year (January 1st)
start_of_year = pd.Timestamp(year=current_date.year, month=1, day=1)

# Calculate the number of days since the start of the year
days_since_start_of_year = (current_date_timestamp - start_of_year).days

# Print the result
print(f"Number of days since the start of the year: {days_since_start_of_year}")