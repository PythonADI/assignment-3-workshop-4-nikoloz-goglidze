phone_numbers = []
country_code = input("enter country code")
num_numbers = int(input("How many phone numbers would you like to add to the list? "))
for i in range(num_numbers):
    phone_number = input(f"Enter phone number {i+1}: ")
    phone_numbers.append(phone_number)
for number in phone_numbers:
    print(f"Sending message to: {country_code} {number}")
cost_massige = 0.10
total_cost = 0
for number in phone_numbers:
    print(f"Sending message to: {number}")
    total_cost += cost_massige
print(f"Total cost of sending messages: ${total_cost}")
premium_customer= input("")
print(premium_customer)
if premium_customer == "yes":
    print ( f'Total cost after discount{total_cost}')