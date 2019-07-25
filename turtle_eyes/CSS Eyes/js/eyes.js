window.onload = function(e){ 
    makeScreenDoor(75);
}

function makeScreenDoor(numberOfRows) {
    var flexRow = document.createElement("div");
    flexRow.className = 'flex-grow-1';
    document.getElementById("screenDoor").appendChild(flexRow);

    for (let index = 0; index < numberOfRows; index++) {
        var darkRow = document.createElement("div");
        darkRow.className = 'blackRow';
        darkRow.setAttribute("style", " z-index: 2;");

        var flexRow = document.createElement("div");
        flexRow.className = 'flex-grow-1';

        document.getElementById("screenDoor").appendChild(darkRow);
        document.getElementById("screenDoor").appendChild(flexRow);
    }
}

function AngryEyes(){
    setTimeout(function(){
        document.getElementById("circleLeft").classList.remove('angryLeft');
        document.getElementById("circleRight").classList.remove('angryRight');
    }, 6000);
    document.getElementById("circleLeft").classList.add('angryLeft');
    document.getElementById("circleRight").classList.add('angryRight');
}

function Blink(){
    setTimeout(function(){
        document.getElementById("circleLeft").classList.remove('blinkLeft');
        document.getElementById("circleRight").classList.remove('blinkRight');
    }, 1000);
    document.getElementById("circleLeft").classList.add('blinkLeft');
    document.getElementById("circleRight").classList.add('blinkRight');
}