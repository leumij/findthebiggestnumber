# Ask user to input 3 numbers. Find and print the biggest number using only if-else statement.

# pseudocode

# ask user 3 number for input
print("Enter 3 number and let's determine the greatest among the three")
number_one = int(input("Enter your First Number: "))
number_two = int(input("Enter your Second Number: "))
number_three = int(input("Enter your Third Number: "))

# find the biggest number
if number_one > number_two and number_one > number_three:
    greatest = number_one

elif number_two > number_one and number_two > number_three:
    greatest = number_two

else:
     greatest = number_three

# print the biggest number
print("The greatest among the numbers you have entered {},{} and {} is number{}" .format(number_one,number_two,number_three, greatest))
