from flask import Flask, render_template
app = Flask(__name__)

@app.route("/play")
def play():
    return render_template("index.html")

@app.route("/play/<int:x>")
def level(x):
    return render_template("index2.html", x=x)

@app.route("/play/<int:x>/<color>")
def level3(x,color):
    
    return render_template("index3.htm",x=x, y=color)



if __name__=="__main__":
    app.run(debug=True)