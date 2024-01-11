# Ask user to input 3 numbers. Find and print the biggest number using only if-else statement.

# pseudocode

# ask user 3 number for input
print("Enter 3 number and let's determine the greatest among the three")
number_one = int(input("Enter your First Number: "))
number_two = int(input("Enter your Second Number: "))
number_three = int(input("Enter your Third Number: "))

# find the biggest number
if number_one > number_two and number_one > number_three:
    print("Number one largest number, which is number" , number_one)

elif number_two > number_one and number_two > number_three:
    print("Number two is the largest number, which is number" , number_two)

else:
    print("Number three is the largest number, which is number" , number_three)

# print the biggest number