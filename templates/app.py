from flask import Flask, render_template
from typing_trainer import home, level_page, handle_typing, progress_summary

app = Flask(__name__)

# Routes
app.add_url_rule("/", "home", home)
app.add_url_rule("/level/<int:level_number>", "level_page", level_page)
app.add_url_rule("/progress", "progress_summary", progress_summary, methods=["GET"])
app.add_url_rule("/handle_typing", "handle_typing", handle_typing, methods=["POST"])

# About Page Route
@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)

