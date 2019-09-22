from flask import Flask, request, render_template
import math
from InputForm import InputForm

app = Flask(__name__)

#@app.route('/')
#def index():
#    return render_template('index.html')



@app.route('/calculate', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    template_name = 'view0'
    if request.method == 'POST' and form.validate():
        result = calculate(form.w.data, form.h.data)
    else:
        result = None

    return render_template(template_name + '.html',
                           form=form, result=result)



def calculate(weight, height):
    BMI = 703 * weight / (math.pow(height, 2))
    return str("%0.2f" %BMI)


if __name__ == '__main__':
    app.run(debug=True)
