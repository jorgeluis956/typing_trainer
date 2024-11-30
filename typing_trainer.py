from flask import request, jsonify, render_template

# Levels dictionary
levels = {
    1: 'print("Hello World!")',
    2: 'print(1 + 1)',
    3: 'age = 12\nprint(age)',
    4: 'languages = ["Python", "Java", "C"]\nprint(languages)',
    5: 'location = (3, 5)\nprint(location)',
    6: 'groceries = {"apples": 3, "milk": 2, "bread": 1}\nprint(groceries)',
    7: 'for i in range(3):\n    print(i)',
    8: 'cities = ["New York", "Paris"]\nfor i in cities:\n    print(i)',
}

# Global dictionary to track user progress
user_progress = {}

# Home page route
def home():
    return render_template("home.html", levels=levels)

# Display the specific level page
def level_page(level_number):
    level_code = levels.get(level_number)
    if not level_code:
        return "Level not found!", 404
    return render_template(
        "practice.html", level_number=level_number, level_code=level_code
    )

# Handle typing practice logic via AJAX
def handle_typing():
    data = request.json
    level_number = int(data.get("level_number"))
    user_input = data.get("user_input", "")
    level_code = levels.get(level_number, "")

    # Normalize quotes to avoid issues with different keyboard styles
    user_input = user_input.replace("“", "\"").replace("”", "\"")
    level_code = level_code.replace("“", "\"").replace("”", "\"")

    # Compare user input with the target code
    is_correct = user_input == level_code
    mistakes = sum(
        1 for a, b in zip(user_input, level_code) if a != b
    ) + abs(len(level_code) - len(user_input))

    # Save progress if completed
    if is_correct:
        time_taken = float(data.get("time_taken", 0))
        user_progress[level_number] = {
            "time_taken": round(time_taken, 2),
        }
        return jsonify({"is_correct": True, "message": "Level completed!"})

    # Provide feedback for incorrect typing
    return jsonify(
        {"is_correct": False, "message": "Keep going!"}
    )

# Display progress summary
def progress_summary():
    return render_template("progress.html", progress=user_progress)

