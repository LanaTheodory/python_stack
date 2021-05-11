from flask import Flask , render_template

app = Flask(__name__)

@app.route('/<int:x>')
def index1(x=8 , y=8):
    return render_template("index.html" ,x=x, y=y) 

@app.route('/<int:x>/<int:y>')
def index2(x=8 , y=8):
    return render_template("index.html" ,x=x, y=y)


@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def index3(x=8 , y=8,  color1 =" white" , color2 = "black"):
    return render_template("index.html" ,x=x, y=y, color1= color1, color2= color2)


if __name__== "__main__":
    app.run(debug=True)
   