document.addEventListener('DOMContentLoaded', () => {
    const levelSelect = document.getElementById('level-select');
    const targetCode = document.getElementById('target-code');
    const userInput = document.getElementById('user-input');
    const feedback = document.getElementById('feedback');
    const submitBtn = document.getElementById('submit-btn');

    // Fetch levels from the server
    fetch('/get-levels')
        .then(response => response.json())
        .then(data => {
            Object.keys(data).forEach(level => {
                const option = document.createElement('option');
                option.value = level;
                option.textContent = `Level ${level}`;
                levelSelect.appendChild(option);
            });
        });

    // Update target code on level change
    levelSelect.addEventListener('change', () => {
        fetch('/get-levels')
            .then(response => response.json())
            .then(data => {
                targetCode.textContent = data[levelSelect.value];
            });
    });

    // Submit user input and evaluate
    submitBtn.addEventListener('click', () => {
        const startTime = Date.now();

        fetch('/evaluate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                level_number: levelSelect.value,
                user_input: userInput.value,
                time_taken: (Date.now() - startTime) / 1000
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                feedback.textContent = `Success! Time: ${data.time_taken}s, Mistakes: ${data.mistakes}`;
                feedback.style.color = 'green';
            } else {
                feedback.textContent = `Try Again! Mistakes: ${data.mistakes}`;
                feedback.style.color = 'red';
            }
        });
    });
});
