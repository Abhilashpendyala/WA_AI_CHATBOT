from flask import Flask

#__name__ is default variable in python, set to "main" when the script is run directly, or else will
# set to the "file name/module" name

app=Flask(__name__)  # creates instance of web application and tells flask from where to fetch the info

#app.run(host="0.0.0.0",port=5000) #0.0.0.0 tells flask to bind all network interfaces 
#this makes ur code to accept connections from any ip on your netorks if reachable --> if running using script

# flask --app flask_local run --host=0.0.0.0 --port=5000 ( if running flask from cli)

@app.route("/")
def printfun():
    return "<p>webserver running</p>"   #serves static html file

## Run the script in terminal using "flask --app flask_local run"
#use nginix for static content files and gunicorn for app server in production