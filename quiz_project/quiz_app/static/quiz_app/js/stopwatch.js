const stopwatch = document.getElementById("stopwatch");

let seconds = 10;
let timer;

function updateSeconds(){
    seconds--;
    stopwatch.textContent = seconds;
    if(seconds == 0){
        let quizId = window.location.pathname.split('/')[2];
        window.location.href = "/quiz_result/" + quizId + "/";
    }
}

timer = setInterval(updateSeconds, 1000);

