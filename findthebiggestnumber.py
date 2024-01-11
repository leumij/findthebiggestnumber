# Ask user to input 3 numbers. Find and print the biggest number using only if-else statement.

from flask import Flask, render_template, request

app = Flask(__name__)

# pseudocode

# ask user 3 number for input
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
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

        return render_template('result.html', greatest=greatest)   

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)




