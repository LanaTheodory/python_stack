from flask import Flask, render_template, request , session, redirect

app = Flask(__name__)
app.secret_key = "lana"

@app.route("/")
def counter():
    session["count"] 
    if 'count' in session:
        session["count"] += 1

        counts = session["count"]

    return render_template("index.html", counts = counts)

@app.route("/destroy")
def destroy():
    session["count"] = 0
    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)

