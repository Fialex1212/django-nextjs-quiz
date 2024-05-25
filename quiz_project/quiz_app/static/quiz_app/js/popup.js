document.getElementById("opetSettings").addEventListener("click", function() {
    document.getElementById("popup").style.display = "flex";
    document.getElementById("blockout").style.display = "block";
});

document.getElementById("change-username").addEventListener("click", function(){
    document.getElementById("popup").style.display = "none";
    document.querySelector(".popup-change-username").style.display = "flex";
});

document.getElementById("change-email").addEventListener("click", function(){
    document.getElementById("popup").style.display = "none";
    document.querySelector(".popup-change-email").style.display = "flex";
});

document.getElementById("change-password").addEventListener("click", function(){
    document.getElementById("popup").style.display = "none";
    document.querySelector(".popup-change-password").style.display = "flex";
});

function closeButton(){
    document.getElementById("popup").style.display = "none";
    document.querySelector(".popup-change-username").style.display = "none";
    document.querySelector(".popup-change-email").style.display = "none";
    document.querySelector(".popup-change-password").style.display = "none";
    document.getElementById("blockout").style.display = "none";
};

function backButton(){
     document.querySelector(".popup").style.display = "flex";
    document.querySelector(".popup-change-username").style.display = "none";
    document.querySelector(".popup-change-email").style.display = "none";
    document.querySelector(".popup-change-password").style.display = "none";
};

document.getElementById("blockout").addEventListener("click", function(){
    document.getElementById("popup").style.display = "none";
    document.querySelector(".popup-change-username").style.display = "none";
    document.querySelector(".popup-change-email").style.display = "none";
    document.querySelector(".popup-change-password").style.display = "none";
    document.getElementById("blockout").style.display = "none";
});