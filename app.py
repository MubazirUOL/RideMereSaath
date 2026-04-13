print("Welcome to RideMereSaath! A Car Pooling App developed for your ease of commutating...")

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return "About Page..."

@app.route("/contact")
def contact():
    return "Contact us at below..."

@app.route("/ride/<user>")
def ride(user):
    return render_template("ride.html", user=user)

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if(request.method == "POST"):
        user = request.form["username"]
        return f"Good Day {user} !"
    return render_template("signup.html")

@app.route("/user/<name>")
def user(name):
    return render_template("index.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)
