print("Welcome to the tip calculator.")

bill = input('What was the total bill? ')
tip = input('What percentage tip would you like to give? ')
amount_people = input('How many people is there to split the bill? ')

total_cost = round(float(bill) + (float(bill) / 100 * float(tip)), 2)
cost_per_person = round(total_cost / int(amount_people), 2)

print(f"the total cost including the tip is: £{total_cost:.2f} and costs £{cost_per_person:.2f} per person.")