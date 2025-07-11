# Prompt the user for their monthly income
monthly_income = int(input("Enter your monthly income: "))

# Prompt the user for their total monthly expenses
monthly_expenses = int(input("Enter your total monthly expenses: "))

# Calculate the monthly savings
monthly_savings = monthly_income - monthly_expenses

# a simple annual interest rate of 5%
annual_interest_rate = 5 / 100

# projected savings after one year
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * annual_interest_rate)

# Display the result
print("Your monthly savings are:", "$" + str(monthly_savings) + ".")
print("Projected savings after one year, with interest, is: ", "$" + str(int(projected_savings)) + ".")