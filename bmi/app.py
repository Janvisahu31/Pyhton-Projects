from flask import Flask, render_template, request
from flask_cors import CORS
from webui import WebUI

app = Flask(__name__)
CORS(app, methods=["GET", "POST"])
ui = WebUI(app, debug=True)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/bmi", methods=["GET", "POST"])
def calculate():
    if request.method == "POST":
        try:
            print("Received POST request to /bmi")
            weight = float(request.form.get("weight"))
            height = float(request.form.get("height"))
            print("Weight:", weight)
            print("Height:", height)
            if weight and height:
                bmi = round(weight / ((height / 100) ** 2), 2)
                print("BMI:", bmi)
                return render_template("index.html", bmi=bmi)
            else:
                error = "Please enter both weight and height."
                return render_template("index.html", error=error)
        except ValueError:
            error = "Please enter valid numerical values for weight and height."
            return render_template("index.html", error=error)
    else:
        return "Method not allowed"

if __name__ == "__main__":
    ui.run(debug=True)
