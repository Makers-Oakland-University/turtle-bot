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