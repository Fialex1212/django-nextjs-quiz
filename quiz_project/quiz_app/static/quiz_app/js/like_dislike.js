function likeQuiz(quizId) {
    fetch(`/quiz_like/${quizId}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': '{{ csrf_token }}', // Ensure CSRF token is included
            'Content-Type': 'application/json'
        },
        credentials: 'same-origin' // Include cookies in the request
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        // Handle the response as needed
        console.log('Quiz liked successfully');
        // Optionally, you can reload the page or update the UI
    })
    .catch(error => {
        console.error('Error:', error);
        // Handle errors, e.g., display an error message
    });
}

function dislikeQuiz(quizId) {
    fetch(`/quiz_dislike/${quizId}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': '{{ csrf_token }}', // Ensure CSRF token is included
            'Content-Type': 'application/json'
        },
        credentials: 'same-origin' // Include cookies in the request
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        // Handle the response as needed
        console.log('Quiz disliked successfully');
        // Optionally, you can reload the page or update the UI
    })
    .catch(error => {
        console.error('Error:', error);
        // Handle errors, e.g., display an error message
    });
}
