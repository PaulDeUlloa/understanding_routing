from flask import Flask, render_template  # Import Flask to allow us to create our app

app = Flask(__name__)  # Create a new instance of the Flask class called "app"


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/Dojo")
def dojo():
    return "Dojo"


@app.route("/say/<name>")
def say(name):
    return "Hi, " + name


@app.route("/repeat/<int:num>/<string:word>")
def repeat(num, word):
    output = ""
    for i in range(0, num):
        output += f"<p>{word}</p>"
    return output


@app.route("/career")
def career():
    return f"Sorry! no response. Try again."


if (
    __name__ == "__main__"
):  # Ensure this file is being run directly and not from a different module
    app.run(debug=True, host="localhost", port=8000)  # Run the app in debug mode.
