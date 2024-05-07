function likeQuiz(quizId) {
    fetch(`/quiz_like/${quizId}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': '{{ csrf_token }}',
            'Content-Type': 'application/json'
        },
        credentials: 'same-origin'
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        // Update liked_quizzes data
        liked_quizzes.push(quizId);
        // Update UI to reflect the like action
        document.getElementById(`like_button_${quizId}`).src = "/media/site/heart_full.svg";
        console.log('Quiz liked successfully');
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function dislikeQuiz(quizId) {
    fetch(`/quiz_dislike/${quizId}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': '{{ csrf_token }}',
            'Content-Type': 'application/json'
        },
        credentials: 'same-origin'
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        // Remove quizId from liked_quizzes data
        liked_quizzes = liked_quizzes.filter(id => id !== quizId);
        // Update UI to reflect the dislike action
        document.getElementById(`like_button_${quizId}`).src = "/media/site/heart_empty.svg";
        console.log('Quiz disliked successfully');
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
