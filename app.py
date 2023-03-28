import csv
import datetime
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/expenses", methods=["POST"])
def add_expense():
    description = request.form.get("description")
    amount = request.form.get("amount")
    date = datetime.datetime.now()

    with open("expenses.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([description, amount, date])

    return redirect("/expenses")

@app.route("/expenses")
def expenses():
    expenses_list = []

    with open("expenses.csv", newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            expenses_list.append(row)

    return render_template("expenses.html", expenses=expenses_list)

if __name__ == "__main__":
    app.run(debug=True)
