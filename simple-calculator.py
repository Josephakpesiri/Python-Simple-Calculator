print("======= Welcome to My Simple Python Calculator =======")
#collect data from user
first_number = input("Enter first number: ")
second_number = input("Enter second number: ")
print()
#convert and store data as whole numbers while carrying out operations
addition = int(first_number) + int(second_number)
subtraction = int(first_number) - int(second_number)
multiplication = int(first_number) * int(second_number)
division = int(first_number) / int(second_number)
#display answers
print("======= Here's Your Results =======")
print(f"Addition: {addition} \nSubtraction: {subtraction} \nMultiplication: {multiplication} \nDivision: {division}")
