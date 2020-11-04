from flask import Flask, render_template
#create a Flask instance
app = Flask(__name__)

#connects default URL to a function
@app.route('/')
def home():
    #Flask import uses Jinga to render HTML
    return render_template("home.html")

@app.route('/aboutus/')
def aboutus():
    #Flask import uses Jinga to render HTML
    return render_template("aboutus.html")

@app.route('/aboutus/aditi/')
def aboutus():
    #Flask import uses Jinga to render HTML
    return render_template("aboutus.html")

@app.route('/aboutus/carter/')
def aboutus():
    #Flask import uses Jinga to render HTML
    return render_template("aboutus.html")

@app.route('/aboutus/isai/')
def aboutus():
    #Flask import uses Jinga to render HTML
    return render_template("aboutus.html")

@app.route('/contents/mustafa/')
def contents():
    #Flask import uses Jinga to render HTML
    return render_template("contents.html")

@app.route('/aboutdn/sophie/')
def delnorte():
    #Flask import uses Jinga to render HTML
    return render_template("aboutdn.html")

@app.route('/aboutsd/')
def sandiego():
    #Flask import uses Jinga to render HTML
    return render_template("aboutsd.html")

@app.route('/playground/')
def playground():
    #Flask import uses Jinga to render HTML
    return render_template("dropdown.html")

@app.route('/aboutsd/history/')
def sdhistory():
    #Flask import uses Jinga to render HTML
    return render_template("sdhistory.html")

@app.route('/aboutsd/landmarks/')
def sdlandmarks():
    #Flask import uses Jinga to render HTML
    return render_template("sdlandmarks.html")

@app.route('/aboutsd/tourist/')
def sdtourist():
    #Flask import uses Jinga to render HTML
    return render_template("sdtourist.html")

@app.route('/aboutsd/restaurant/')
def sdrestaurant():
    #Flask import uses Jinga to render HTML
    return render_template("sdrestaurant.html")

if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True, port='5000', host='127.0.0.1')
