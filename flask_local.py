from flask import Flask

#__name__ is default variable in python, set to "main" when the script is run directly, or else will
# set to the "file name/module" name

app=Flask(__name__)  # creates instance of web application

@app.route("/")
def printfun():
    return "<p>webserver running</p>"

