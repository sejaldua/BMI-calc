flask_app = Flask('BMI Calculator')
app = Api(app = flask_app)
name_space = app.namespace('main', descrption='Main APIs')

