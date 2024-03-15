# accepts user input to create a list of integers
user_input = input("Enter a list of numbers (separate them with a spaces): ")
numbers = user_input.split()
total_sum = 0
for num in numbers:
    try:
        total_sum += int(num)
    except ValueError:
        print(f"Invalid input: '{num}' is not a valid integer.")
print(f"The sum of the entered integers is: {total_sum}")