from flask import Flask,render_template


# Create Flask Instance
app=Flask(__name__)


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

if __name__== "__main__":
    app.run(debug=True)