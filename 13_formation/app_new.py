# Johnson Li
# SoftDev1 pd8
# K13 -- Echo Echo Echo 
# 2018-09-27

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    # root route with form
    return render_template("form.html")

@app.route("/auth", ['GET', 'POST'])
def authenticate():
    # each needed field is assigned to a var
    username = request.args['username']
    reqMethod = request.method 
    greeting = "HI " + username.upper()
    print(reqMethod)
    if reqMethod == 'GET':
        username = request.args['username']
    else:
        username = request.form['username']

    # return the html page using a template
    return render_template("response.html", 
                            username = username, 
                            reqMethod = reqMethod, 
                            greeting = greeting);

app.debug = True;
app.run()

if __name__ == "__main__":
    app.debug = True;
    app.run()
