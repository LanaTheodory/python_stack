from flask import Flask, render_template , request , redirect
app=Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users' , methods=["POST"])
def index2():
    
    return render_template("info.html", name = request.form["name"] , email = request.form["email"] , comments = request.form["comments"] ,lang = request.form["language"] , location = request.form["location"])


if __name__ == "__main__":
    app.run(debug=True)