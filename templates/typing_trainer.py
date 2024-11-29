def handle_typing():
    data = request.json
    level_number = int(data.get("level_number"))
    user_input = data.get("user_input", "")
    level_code = levels.get(level_number, "")

    # Compare user input with the target code
    is_correct = user_input == level_code
    mistakes = sum(1 for a, b in zip(user_input, level_code) if a != b) + abs(len(level_code) - len(user_input))

    # Save progress if completed
    if is_correct:
        time_taken = float(data.get("time_taken", 0))
        user_progress[level_number] = {
            "time_taken": round(time_taken, 2),
            "mistakes": mistakes,
        }
        return jsonify({
            "is_correct": True,
            "message": "Level completed! Click 'Back to Main Menu' to return."
        })
    
    return jsonify({
        "is_correct": False,
        "mistakes": mistakes,
        "message": f"Keep going! {mistakes} mistakes so far."
    })

