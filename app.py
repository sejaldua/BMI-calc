#!python3

from flask import Flask, render_template, request
import math
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = ''
    if request.method == 'POST' and 'weight' in request.form:
        weight = float(request.form.get('weight'))
        height = float(request.form.get('height'))
        if weight > 0 and height > 0:
            bmi = calc_bmi(weight, height)
    return render_template("page.html",
	                        bmi=bmi)

def calc_bmi(weight, height):
    return round(703 * weight / (math.pow(height, 2)), 2)

if __name__ == '__main__':
    app.run(debug=True)