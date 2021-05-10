from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return 'Hello World!' 

@app.route("/lana")
def hi():
    return "bye lana"

@app.route("/<name>")
def bye(name):
    return name

@app.route('/repeat/<int:times>/<name>')
def repeat(times,name):
    str=name
    for i in range(0,times,1):
        str +='<br>'+ str 
      
    return str
    


    


if __name__=="__main__":      
    app.run(debug=True) 