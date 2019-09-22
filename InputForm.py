from wtforms import Form, FloatField, validators

class InputForm(Form):
    w = FloatField(
        label='weight (lbs)', default=0.0,
        validators=[validators.InputRequired()])
    h = FloatField(
        label='height (in)', default=0.0,
        validators=[validators.InputRequired()])
    
