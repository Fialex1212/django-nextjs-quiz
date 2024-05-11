function likeQuiz(quizId, quizTitle) {
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

        var div = document.createElement('div');
        div.style.backgroundColor = "white";
        div.style.position = "fixed";
        div.style.left = "50px";
        div.style.top = "50px";
        div.textContent = "You liked quiz " + quizTitle;
        
        // Append the div to the document body or any other desired element
        var existingDivs = document.querySelectorAll('.like-message');
        var topPosition = 50 + (existingDivs.length * 50); // Increment by 50 pixels for each existing div
        div.style.top = topPosition + "px";
        
        div.textContent = "You liked quiz " + quizTitle;
        div.classList.add('like-message'); // Add a class to identify these divs
        
        // Append the div to the document body or any other desired element
        document.body.appendChild(div);

        setTimeout(function(){
            document.body.removeChild(div);
        }, 3000)
        // Optionally, you can reload the page or update the UI
    })
    .catch(error => {
        console.error('Error:', error);
        // Handle errors, e.g., display an error message
    });
}

function dislikeQuiz(quizId, quizTitle) {
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
        
        var div = document.createElement('div');
        div.style.backgroundColor = "white";
        div.style.position = "fixed";
        div.style.left = "50px";
        div.style.top = "50px";
        div.textContent = "You disliked quiz " + quizTitle;
        
        var existingDivs = document.querySelectorAll('.like-message');
        var topPosition = 50 + (existingDivs.length * 50);
        div.style.top = topPosition + "px";
        
        div.textContent = "You disliked quiz " + quizTitle;
        div.classList.add('like-message');
        
        document.body.appendChild(div);

        setTimeout(function(){
            document.body.removeChild(div);
        }, 3000)

    })
    .catch(error => {
        console.error('Error:', error);
        // Handle errors, e.g., display an error message
    });
}