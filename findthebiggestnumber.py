# Ask user to input 3 numbers. Find and print the biggest number using only if-else statement.

from flask import Flask, render_template, request

app = Flask(__name__)

# pseudocode

# ask user 3 number for input

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/find_greatest', methods=['POST'])
def find_greatest():
        number_one = int(request.form[''])
        number_two = int(request.form[''])
        number_three = int(request.form[''])
                
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




