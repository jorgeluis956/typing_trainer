from flask import Flask, render_template
from typing_trainer import level_page, handle_typing, progress_summary

app = Flask(__name__)

# Levels dictionary
levels = {
    1: "Hello World!",
    2: "Adding Numbers",
    3: "Variables",
    4: "Lists",
    5: "Tuples",
    6: "Dictionaries",
    7: "For Loops",
    8: "More Loops"
}

# Routes
@app.route("/")
def home():
    return render_template("home.html", levels=levels)

app.add_url_rule("/level/<int:level_number>", "level_page", level_page)
app.add_url_rule("/progress", "progress_summary", progress_summary, methods=["GET"])
app.add_url_rule("/handle_typing", "handle_typing", handle_typing, methods=["POST"])

# About Page Route
@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)

