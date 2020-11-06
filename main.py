from flask import Flask, render_template

import data

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
    return render_template("aboutus.html", data=data.aditis_video())

@app.route('/aboutus/aditi/')
def aditi():
    #Flask import uses Jinga to render HTML
    return render_template("aditi.html", data=data.aditis_video())

@app.route('/aboutus/carter/')
def carter():
    #Flask import uses Jinga to render HTML
    return render_template("carter.html", data=data.carters_video())

@app.route('/aboutus/isai/')
def isai():
    #Flask import uses Jinga to render HTML
    return render_template("isai.html", data=data.isais_video())

@app.route('/aboutus/mustafa/')
def mustafa():
    #Flask import uses Jinga to render HTML
    return render_template("mustafa.html", data=data.mustafas_video())

@app.route('/aboutus/sophie/')
def sophie():
    #Flask import uses Jinga to render HTML
    return render_template("sophie.html", data=data.sophies_video())

@app.route('/contents/')
def contents():
    #Flask import uses Jinga to render HTML
    return render_template("contents.html")

@app.route('/aboutdn/')
def aboutdn():
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

@app.route("/project/journal")
def journal_route():
    return render_template("sophie.html", data=data.journal())

if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True, port='5000', host='127.0.0.1')
