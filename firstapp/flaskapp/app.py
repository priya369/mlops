from flask import Flask
app= Flask(__name__)

@app.route('/')
def hello():
    return "welcome to my machine learning model"

if __name__=='__main__':
    app.run(debug=True)
    