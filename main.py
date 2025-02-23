from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


# Create Flask Instance
app=Flask(__name__)
app.config['SECRET_KEY'] = "hhHVHVK@KHKHKHKH222hkkhkh1"


# Create a form class
class NameForm(FlaskForm):
    name = StringField("What's Your Name",validators=[DataRequired()])
    address = StringField("Address", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route('/')
def index():
    stuff= "Thus is bold Text"
    faviorites=["Pepperoni","Cheese","none"]
    return render_template("index.html",
                           stuff=stuff,
                           faviorites=faviorites)


@app.route('/user/<name>')
def user(name):
    return render_template("user.html",name=name)

# Create Custom Error pages
#Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("404.html"), 500

# Create Name Page
@app.route('/name',methods=['GET','POST'])
def name():
    name = None
    address=None
    form = NameForm()
    # validate Form
    if form.validate_on_submit():
        name= form.name.data
        address=form.address.data
        form.name.data = ' '
    
    return render_template("name.html",
                           name=name,
                           address=address,
                           form=form)


if __name__== "__main__":
    app.run(debug=True)